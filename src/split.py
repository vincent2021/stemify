import spleeter.separator as spleeter


def split(input_file, output_dir, stem):
    """
    Split the audio file 'input_file' according to 'stem' and save result in 'output_dir'
    :param input_file:       audio file
    :param output_dir:  output directory
    :param stem:        (Int) Can be either :
                        2: split vocals and other
                        4: split vocals, drum, bass, other
                        5: split vocals, drum, bass, piano, other
    """
    if stem != 2 and stem != 4 and stem != 5:
        raise AttributeError("Wrong stem value.")
    separator = spleeter.Separator(f'spleeter:{stem}stems')
    separator.separate_to_file(input_file, output_dir)
