# Writing assessment

Hello there, 

Thanks for writing in. I’m sorry to see that you’re running into a `NoneType` error when trying to transcribe your podcast with speaker labels. Let me help you get this sorted out. 

The issue is likely that the URL you’re using isn’t a direct link to an audio file (like a `.mp3` or `.wav`). AssemblyAI needs a direct audio file link, but it looks like the URL you shared points to a webpage instead, so it won’t work for transcription.

You can get a direct link to the audio file from listennotes from the `More` button on the right side, and then by clicking `Download audio`

![Screenshot 2024-11-18 at 11.40.19 AM.png](Writing%20assessment%201427e96158fc800e9014edf14950eb07/Screenshot_2024-11-18_at_11.40.19_AM.png)

This will give you the following link, which you can use instead of the one currently in your code:

[https://d3ctxlq1ktw2nl.cloudfront.net/staging/2024-3-27/0473da78-47d1-a6a8-7d64-4e939fb23c7e.m4a](https://d3ctxlq1ktw2nl.cloudfront.net/staging/2024-3-27/0473da78-47d1-a6a8-7d64-4e939fb23c7e.m4a)

Also, to avoid `NoneType` errors if there are issues with the transcription, you can add a check to make sure `transcript.utterances` exists before looping through it. Here’s how your updated code might look:

```jsx
import assemblyai as aai

aai.settings.api_key = "f7b91a0f92764e2db429300738fc13c1"

# link to direct audio file
audio_url ="https://d3ctxlq1ktw2nl.cloudfront.net/staging/2024-3-27/0473da78-47d1-a6a8-7d64-4e939fb23c7e.m4a"
config = aai.TranscriptionConfig(
speaker_labels=True,
)

transcript = aai.Transcriber().transcribe(audio_url, config)

# Loop through each utterance and print speaker labels and text
if transcript.utterances:
    for utterance in transcript.utterances:
        print(f"Speaker {utterance.speaker}: {utterance.text}")
else:
    print("No utterances found.")
```

This should get you back on track and allow you transcribe the podcast. I hope this helps and please let me know if you have any further questions. I’m here to help.

Best regards, 

Jordy