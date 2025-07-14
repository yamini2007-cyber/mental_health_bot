import random

MOOD_RESPONSES = {
    "sad": [
        "I'm really sorry you're feeling like this.",
        "It’s okay to cry. Emotions make us human.",
        "Take your time. You don’t have to be okay right now.",
        "You’re not alone. I’m here with you.",
        "Would you like to try a calming breathing exercise?",
        "Even the darkest night ends with sunrise.",
        "Don’t bottle it up. You matter.",
        "Feeling sad is not a weakness—it's valid.",
        "You’re stronger than you think, even if it doesn’t feel like it now.",
        "Sometimes, talking helps. I'm listening."
    ],

    "angry": [
        "Anger is valid. Let's try to express it safely.",
        "Want to vent? I’m here to listen.",
        "Take a deep breath, count to five, and let's talk.",
        "You don’t have to bottle it all in.",
        "Punching a pillow helps too 😅",
        "Your feelings are real. You're not wrong for being mad.",
        "Let it out. Don’t let it eat you up.",
        "Sometimes, even silence feels loud, right?",
        "I'm not judging you. I'm here for you.",
        "Let’s shift the energy to something that soothes you."
    ],

    "anxious": [
        "Let’s pause and take a few slow breaths together.",
        "You’re safe here. This feeling will pass.",
        "Anxiety lies. You’re doing better than you think.",
        "Ground yourself. Look around and name 3 things you see.",
        "This moment will not last forever.",
        "Let’s slow things down, one step at a time.",
        "You are not your anxiety.",
        "Even overthinking can’t stop your strength.",
        "Your mind is racing, but I’m here to hold space.",
        "Close your eyes. Inhale 4, hold 4, exhale 4."
    ],

    "happy": [
        "That’s wonderful to hear! 😊",
        "Keep smiling. It suits you!",
        "Your joy is contagious!",
        "Let's celebrate this good mood 🥳",
        "Enjoy this moment fully!",
        "Happiness looks great on you.",
        "Whatever you're doing, keep doing it!",
        "I love this energy! 🔥",
        "Don't forget to share that smile today!",
        "May this happiness stay with you longer!"
    ],

    "neutral": [
        "Hey, I'm here with you.",
        "How are you really feeling?",
        "Sometimes 'fine' hides a lot. You can talk to me.",
        "Let’s check in with your thoughts.",
        "It’s okay to not know how you feel.",
        "Even small talks matter.",
        "I’m just a bot, but I care.",
        "Mood swings happen. Let's talk about it.",
        "Take a breath. Maybe even a break.",
        "We can sit here quietly, or talk—your choice."
    ]
}

