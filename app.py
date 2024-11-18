import assemblyai as aai

# Set the API key
aai.settings.api_key = "f7b91a0f92764e2db429300738fc13c1"

# Set the transcriber
transcriber = aai.Transcriber()

# Audio URL
audio_url = "https://github.com/AssemblyAI-Examples/audio-examples/raw/main/20230607_me_canadian_wildfires.mp3"

# Set up the transcription with speaker labels and sentiment analysis
config = aai.TranscriptionConfig(speaker_labels=True, sentiment_analysis=True)

# Start the transcription
transcript = transcriber.transcribe(audio_url, config)

# Save utterances with speaker labels to `utterances.txt`
def save_utterances(transcript, output_file="utterances.txt"):
    try:
        if not transcript.utterances:
            print("No utterances found in the transcript.")
            return

        with open(output_file, "w") as file:
            for utterance in transcript.utterances:
                file.write(f"Speaker {utterance.speaker}: \"{utterance.text}\"\n\n")
        print(f"Utterances saved to {output_file}")
    except Exception as e:
        print(f"Error saving utterances: {e}")

# Function to calculate and print the percentage of speaking time
def speaking_time(transcript):
    total_time = 0
    speaker_times = {}

    for utterance in transcript.utterances:
        speaker = utterance.speaker
        duration = utterance.end - utterance.start 

        speaker_times[speaker] = speaker_times.get(speaker, 0) + duration
        total_time += duration

    for speaker in sorted(speaker_times):
        percentage = (speaker_times[speaker] / total_time) * 100
        print(f"{speaker} spoke for {percentage:.2f}% of the time.")

# Function to determine the overall sentiment for each speaker
def sentiment(transcript):
    sentiment_counts = {}

    # Count each sentiment for each speaker using `sentiment_analysis`
    for sentiment_result in transcript.sentiment_analysis:
        speaker = sentiment_result.speaker
        sentiment = sentiment_result.sentiment

        # Initialize sentiment counts for each speaker if not already done
        if speaker not in sentiment_counts:
            sentiment_counts[speaker] = {"positive": 0, "neutral": 0, "negative": 0}

        # Increment the count for the specific sentiment
        sentiment_counts[speaker][sentiment.lower()] += 1

    # Determine and print the most common sentiment for each speaker
    for speaker in sorted(sentiment_counts):
        counts = sentiment_counts[speaker]
        max_sentiments = [s for s, count in counts.items() if count == max(counts.values())]

        if len(max_sentiments) > 1:
            sentiment_str = " and ".join(max_sentiments)
            print(f"The overall sentiment for {speaker} was equally {sentiment_str}.")
        else:
            print(f"The overall sentiment for {speaker} was {max_sentiments[0]}.")

# Call the functions
save_utterances(transcript)
speaking_time(transcript)
sentiment(transcript)
