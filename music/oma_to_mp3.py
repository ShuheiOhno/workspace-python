from pydub import AudioSegment
from moviepy.editor import AudioFileClip

import os

def convert_oma_to_mp4(input_oma_file, output_mp4_file):
    try:
        # .omaファイルを読み込み
        audio = AudioSegment.from_file(input_oma_file, format="oma")
        
        # .wavファイルに変換して保存
        wav_file = input_oma_file.replace('.oma', '.wav')
        audio.export(wav_file, format="wav")
        
        # .wavファイルを.mp4に変換して保存
        audio_clip = AudioFileClip(wav_file)
        audio_clip.write_videofile(output_mp4_file, codec='libx264', fps=audio_clip.fps)

        # 一時ファイルを削除
        os.remove(wav_file)

        print(f"Conversion successful: {input_oma_file} -> {output_mp4_file}")
    except Exception as e:
        print(f"Conversion failed: {e}")

# 使用例
if __name__ == "__main__":
    input_oma_file = "input.oma"
    output_mp4_file = "output.mp4"
    convert_oma_to_mp4(input_oma_file, output_mp4_file)



# from pydub import AudioSegment

# def convert_oma_to_mp3(input_file, output_file):
#     try:
#         # .omaファイルを読み込み
#         print("aaaaaaaaaaa")
#         audio = AudioSegment.from_file(input_file, format="oma")
        
#         # .mp3ファイルに変換して保存
#         audio.export(output_file, format="mp3")
        
#         print(f"Conversion successful: {input_file} -> {output_file}")
#     except Exception as e:
#         print(f"Conversion failed: {e}")

# # 使用例
# if __name__ == "__main__":
#     input_file = "input.oma"
#     output_file = "output.mp3"
#     convert_oma_to_mp3(input_file, output_file)
