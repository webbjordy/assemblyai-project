# Writing assessment

Hello there, 

Thanks for writing in. I’m sorry to see that you’re running into a `NoneType` error when trying to transcribe your podcast with speaker labels. Let me help you get this sorted out. 

The issue is likely that the URL you’re using isn’t a direct link to an audio file (like a `.mp3` or `.wav`). AssemblyAI needs a direct audio file link, but it looks like the URL you shared points to a webpage instead, so it won’t work for transcription.

You can get a direct link to the audio file from listennotes from the `More` button on the right side, and then by clicking `Download audio`. This will give you the following link, which you can use instead of the one currently in your code:

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

# Internal note

I started out by just running the code provided to verify the error. Once confirmed, I did some digging in the docs and found that a direct link is required. I tested the code with an audio file link that I know works, and the app ran as expected - confirming my suspicions that the link used by the customer is bad.

I then did some poking around on listennotes and found how to access a direct link to the podcast audio, and added that to the customer’s code. 

I added some more info about best practice of adding a check to avoid `NoneType` errors. By doing this, I learned that it’s important to check the link before spending any time on deeper troubleshooting. I also learned that because the transcription can take some time, it’s important to add the check to avoid errors.

