"""Collect real terminal transcripts inside the Skills Network lab."""
from pathlib import Path
import os
import subprocess
import sys
import tempfile

ROOT = Path(__file__).resolve().parent
OUT = ROOT / 'evidence'


def shell_session(name, commands, directory):
    """Run an actual interactive Python interpreter and preserve its output."""
    result = subprocess.run(
        [sys.executable, '-i'], input='\n'.join(commands) + '\nexit()\n',
        cwd=directory, text=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT,
        env={**os.environ, 'PYTHONSTARTUP': '', 'PYTHON_COLORS': '0'}, check=True,
    )
    transcript = '$ python3\n' + result.stdout
    (OUT / name).write_text(transcript)
    print('\n=== ' + name + ' ===\n' + transcript, flush=True)
    if 'Traceback (most recent call last)' in transcript:
        raise RuntimeError('Live API call failed; transcript is not passing evidence.')


if __name__ == '__main__':
    with tempfile.TemporaryDirectory() as directory:
        Path(directory, 'emotion_detection.py').write_text((OUT / '2a_emotion_detection').read_text())
        shell_session('2b_application_creation', [
            'from emotion_detection import emotion_detector',
            'emotion_detector("I love this new technology.")'], directory)
    with tempfile.TemporaryDirectory() as directory:
        Path(directory, 'emotion_detection.py').write_text((OUT / '3a_output_formatting').read_text())
        shell_session('3b_formatted_output_test', [
            'from emotion_detection import emotion_detector',
            'emotion_detector("I am so happy I am doing this")'], directory)
    shell_session('4b_packaging_test', [
        'from EmotionDetection import emotion_detector',
        'emotion_detector("I hate working long hours")'], ROOT)
    for name, args in [
        ('5b_unit_testing_result', ['-m', 'unittest', '-v', 'test_emotion_detection.py']),
        ('8b_static_code_analysis', ['-m', 'pylint', 'server.py']),
    ]:
        result = subprocess.run([sys.executable, *args], cwd=ROOT, text=True,
                                stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
        transcript = '$ python3 ' + ' '.join(args) + '\n' + result.stdout
        (OUT / name).write_text(transcript)
        print('\n=== ' + name + ' ===\n' + transcript, flush=True)
        result.check_returncode()
