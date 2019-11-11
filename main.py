import spleeter.separator as spleeter


input_file = "raw_data/audio_example.mp3"
output_dir = "output"
separator = spleeter.Separator('spleeter:2stems')
separator.separate_to_file(input_file, output_dir)
