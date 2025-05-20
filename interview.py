import json

questions = [
    "Stress reactivity & resilience - A cherished project is rejected as 'off brief' the night before deadline. Walk me through your inner and outer reactions during the next three hours.",
    "Interpersonal anger regulation - A stranger bumps you hard, blames you aloud, and walks off. How do you handle the next ten minutes?",
    "Social initiation & networking - You arrive alone at a reception full of leaders in your field. Describe the first conversation you start and why you chose that person.",
    "Novelty-seeking & calculated risk - Stand-by seats leave in two hours for a city you've never visited. Explain your decision process.",
    "Imagination & creative ideation - You notice a discarded umbrella while queueing. What's the first unusual story, use, or image that pops into your head?",
    "Handling criticism & self-evaluation - A mentor says your latest work 'shows promise but lacks depth.' Describe your thoughts and actions over the following week.",
    "Moral choice & honesty - At self-checkout the scanner misses an expensive item and you're late for an appointment. What happens next?",
    "Goal planning & grit - You set a six-month fitness goal you've never reached before. Outline the system you create to stay on track, including how you react to a rough week.",
    "Time management vs procrastination - An important application is due in four days and you haven't started. Map out your next 24 hours in detail.",
    "Co-operation vs competition - Two teammates push conflicting ideas in a group project. Explain exactly how you influence the direction.",
    "Empathy & helping behaviour - A colleague quietly tears up after a phone call. Describe what you do, say, and think in the next five minutes.",
    "Trust vs scepticism - A cold-caller offers a lucrative investment. Outline the steps you take to test their credibility.",
    "Autonomy & locus of control - Your travel group can't pick a restaurant. Describe how you steer—or don't steer—the final choice.",
    "Impulsivity vs reflection - A flash sale ends in 15 minutes. Walk me through every thought before you click 'buy' or decide to pass.",
    "Emotional awareness & regulation - A close friend forgets your birthday. Detail your emotional journey from noticing to day's end.",
    "Energy & activity style - Describe a typical unscheduled Saturday from wake-up to bedtime, noting pacing and activity switches.",
    "Aesthetic sensitivity - You walk into an unfamiliar art installation. Explain what you attend to first and the kind of meaning you look for.",
    "Values & worldview - A city proposes replacing car lanes with protected bike lanes, slowing traffic but cutting emissions. Argue your stance and why.",
    "Financial risk orientation - Your savings can go into a guaranteed 2% bond or a volatile stock averaging 8%. Show your reasoning.",
    "Intellectual curiosity & learning style - You stumble on an unfamiliar scientific concept online. Describe the steps you take in the next hour to understand it."
]

responses = {}

print("Personality Insight Interview\n")

for idx, q in enumerate(questions, 1):
    print(f"Question {idx}: {q}")
    answer = input("Your answer: ")
    responses[q] = answer
    print()

with open('responses.json', 'w') as f:
    json.dump(responses, f, indent=2)

print("Interview complete. Ready for analysis.")
