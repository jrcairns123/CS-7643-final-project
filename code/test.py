import torch
import torchaudio
from datasets import load_dataset, Dataset
from torch.utils.data import DataLoader



#%% read an audio file

sample_path = r"E:\GaTech OMS Analytics\Degree Courses\2023 Spring\CS 7643 - Deep Learning\Project\peoples_speech\data\train\07282016HFUUforum_SLASH_07-28-2016_HFUUforum_DOT_mp3_00000.flac"

waveform, sample_rate = torchaudio.load(sample_path)
metadata = torchaudio.info(sample_path)


## tutorial which has functions defined for below: https://pytorch.org/audio/stable/tutorials/audio_io_tutorial.html
# print_stats(waveform, sample_rate=sample_rate)
# plot_waveform(waveform, sample_rate)
# plot_specgram(waveform, sample_rate)
# play_audio(waveform, sample_rate)


#%% load dataset
dataset = load_dataset('MLCommons/peoples_speech', name='validation')

# subset dataset
datasub = dataset['validation'][:4]

ds = Dataset.from_dict(datasub)

device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

ds = ds.with_format("torch", device=device)

dataloader = DataLoader(ds, batch_size=2, shuffle=True)

# limited_ds = dataset['validation'].map(lambda example: {'input': example['audio']['array'], 'text': example['text']}, remove_columns=dataset['validation'].column_names)

