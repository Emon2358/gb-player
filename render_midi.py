import os
from midi2audio import FluidSynth
from pydub import AudioSegment

def process_all_midis(midi_dir="midi", output_dir="output", sf2_path="DMG-CPU1.5.SF2"):
    # FluidSynth インスタンスを生成（ゲームボーイ SoundFont を読み込む）
    fs = FluidSynth(sound_font=sf2_path)

    os.makedirs(output_dir, exist_ok=True)

    for fname in os.listdir(midi_dir):
        if not fname.lower().endswith((".mid", ".midi")):
            continue

        base, _ = os.path.splitext(fname)
        midi_path = os.path.join(midi_dir, fname)
        wav_path  = os.path.join(output_dir, f"{base}.wav")
        mp3_path  = os.path.join(output_dir, f"{base}.mp3")

        print(f"[1/2] Rendering {midi_path} → {wav_path}")
        fs.midi_to_audio(midi_path, wav_path)

        print(f"[2/2] Converting {wav_path} → {mp3_path}")
        AudioSegment.from_wav(wav_path).export(mp3_path, format="mp3")

        print(f"✔ Saved: {mp3_path}\n")

if __name__ == "__main__":
    # 環境変数で上書き可能
    midi_dir   = os.getenv("MIDI_DIR", "midi")
    output_dir = os.getenv("OUTPUT_DIR", "output")
    sf2_path   = os.getenv("SOUND_FONT", "GameBoy.sf2")
    process_all_midis(midi_dir, output_dir, sf2_path)
