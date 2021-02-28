# MOOD-AID

## Inspiration
A lot of people like to read inspiring and enlightening quotes. Quotes tell us of our own value system. Quotes are a fantastic motivational resource. Individuals actually love to read famous quotes, due to the fact that these are concise sentences, expressing wisdom, and awakening motivation, inspiration and happiness. They possess the power to uplift thoughts and feelings.

Now that we’re several months into the COVID-19 pandemic, many of us are feeling the emotional toll of the uncertainty, worry and dramatic changes to our habits and our lives. All of us experiences mood changes a lot of times, we feel unmotivated, lazy and doomed. 

To help boost our moods, I present to you all Mood Aid, a chrome extension which will aid your day with quotes according to your mood!

## What it does

Mood Aid is a ML-powered chrome extension which displays inspiring quotes according to your mood. It uses Sentiment Analysis to rate different quotes for your mood. The user can just click the brighter or gloomier icons to get a brighter or gloomier quote based on their current mood.

## How we built it

This chrome extension is built using javascript. The backend is built using Flask, which performs sentiment analysis on a large dataset of famous motivational quotes to rate them according to their sentiments. The chrome extension sends a request to this flask API in order to get a brighter or gloomier quote whatever the user prefers.
