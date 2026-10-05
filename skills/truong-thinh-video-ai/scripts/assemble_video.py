#!/usr/bin/env python3
"""Render existing clips; no AI API calls.
Usage: assemble_video.py plan.json output.mp4
Plan: {"clips":[{"path":"clip.mp4","start":0,"duration":8}],
       "width":1080,"height":1920,"subtitles":"timed.srt"}
start/duration and subtitles are optional. Paths resolve beside plan.json.
Output must not already exist. Video is fitted with black padding, never cropped.
"""
import argparse
import json
import math
import shutil
import subprocess
import tempfile
from pathlib import Path


def run(args, cwd=None):
    return subprocess.run(args, cwd=cwd, check=True, capture_output=True, text=True)


def probe(path):
    return json.loads(run(['ffprobe', '-v', 'error', '-show_streams',
                           '-show_format', '-of', 'json', str(path)]).stdout)


def render(plan_path, output):
    if not shutil.which('ffmpeg') or not shutil.which('ffprobe'):
        raise ValueError('ffmpeg and ffprobe are required')
    plan_path, output = plan_path.resolve(), output.resolve()
    if output.exists():
        raise ValueError('Output exists; choose a new filename')
    plan = json.loads(plan_path.read_text(encoding='utf-8'))
    width, height = int(plan.get('width', 1080)), int(plan.get('height', 1920))
    if min(width, height) < 2 or max(width, height) > 4096 or width % 2 or height % 2:
        raise ValueError('Width/height must be even, from 2 to 4096')
    clips = plan.get('clips', [])
    if not clips:
        raise ValueError('At least one clip is required')
    subtitles = None
    if plan.get('subtitles'):
        subtitles = (plan_path.parent / plan['subtitles']).resolve()
        if not subtitles.is_file():
            raise ValueError('Subtitle file missing')
    output.parent.mkdir(parents=True, exist_ok=True)
    with tempfile.TemporaryDirectory(prefix='video-assemble-') as temp:
        work = Path(temp)
        names = []
        for i, clip in enumerate(clips):
            source = (plan_path.parent / clip['path']).resolve()
            info = probe(source)
            video = next((s for s in info['streams'] if s['codec_type'] == 'video'), None)
            if video is None:
                raise ValueError(f'No video in clip {i + 1}')
            total = float(video.get('duration', info['format'].get('duration', 0)))
            start = float(clip.get('start', 0))
            duration = float(clip.get('duration', total - start))
            if not all(math.isfinite(x) for x in (total, start, duration)):
                raise ValueError('Invalid duration')
            if start < 0 or duration <= 0 or start + duration > total + .05:
                raise ValueError(f'Invalid trim for clip {i + 1}')
            has_audio = any(s['codec_type'] == 'audio' for s in info['streams'])
            args = ['ffmpeg', '-hide_banner', '-loglevel', 'error', '-nostdin',
                    '-ss', str(start), '-i', str(source)]
            if not has_audio:
                args += ['-f', 'lavfi', '-i', 'anullsrc=r=48000:cl=stereo']
            name = f'part{i:04d}.mp4'
            vf = (f'scale={width}:{height}:force_original_aspect_ratio=decrease:force_divisible_by=2,'
                  f'pad={width}:{height}:(ow-iw)/2:(oh-ih)/2,setsar=1,fps=30')
            args += ['-map', '0:v:0', '-map', '0:a:0' if has_audio else '1:a:0',
                     '-t', str(duration), '-vf', vf, '-af', 'apad',
                     '-c:v', 'libx264', '-preset', 'fast', '-crf', '20',
                     '-pix_fmt', 'yuv420p', '-c:a', 'aac', '-ar', '48000',
                     '-ac', '2', '-movflags', '+faststart', str(work / name)]
            run(args)
            names.append(name)
        (work / 'parts.txt').write_text(''.join(f"file '{name}'\n" for name in names))
        run(['ffmpeg', '-hide_banner', '-loglevel', 'error', '-nostdin',
             '-f', 'concat', '-safe', '1', '-i', 'parts.txt', '-c', 'copy',
             '-movflags', '+faststart', 'merged.mp4'], cwd=work)
        result = work / 'merged.mp4'
        if subtitles:
            shutil.copyfile(subtitles, work / 'captions.srt')
            run(['ffmpeg', '-hide_banner', '-loglevel', 'error', '-nostdin',
                 '-i', 'merged.mp4', '-vf',
                 "subtitles=captions.srt:force_style='FontName=DejaVu Sans,FontSize=20,Outline=2,MarginV=35'",
                 '-c:v', 'libx264', '-preset', 'fast', '-crf', '20',
                 '-c:a', 'copy', '-movflags', '+faststart', 'captioned.mp4'], cwd=work)
            result = work / 'captioned.mp4'
        metadata = probe(result)
        if not any(s['codec_type'] == 'video' for s in metadata['streams']):
            raise ValueError('Rendered output has no video')
        # Exclusive creation avoids overwriting another process's output.
        with result.open('rb') as src, output.open('xb') as dst:
            shutil.copyfileobj(src, dst)
        return {'output': str(output), 'duration': metadata['format']['duration'],
                'width': width, 'height': height, 'captions': bool(subtitles)}


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('plan', type=Path)
    parser.add_argument('output', type=Path)
    args = parser.parse_args()
    try:
        print(json.dumps(render(args.plan, args.output), ensure_ascii=False))
    except subprocess.CalledProcessError as error:
        parser.exit(1, error.stderr[-2000:] + '\n')
    except (ValueError, OSError, KeyError) as error:
        parser.exit(1, str(error) + '\n')
