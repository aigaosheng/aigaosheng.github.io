---
layout: post
title: "Robots Are Learning Faster Than They Are Earning"
description: "Embodied AI got much smarter in two years but has not yet become a big business outside robotaxis and warehouse robots. What works, what is hard, who is winning, and what it means."
date: 2026-10-24 23:00:00 +0800
type: post
published: true
status: publish
categories: [column]
tags:
- Embodied AI
- Robotics
- Humanoid Robots
- Robotaxi
- Physical AI
- AI Hardware
keywords: embodied ai robots 2026, humanoid robot market, robotaxi waymo, warehouse robots amazon, vision language action models, robot reliability, physical intelligence, google deepmind gemini robotics, nvidia groot, unitree ipo, agility robotics digit, robot hands manipulation, moravec paradox, lerobot hugging face, robot safety regulation
permalink: /robots-learning-faster-than-earning/
---

# Robots Are Learning Faster Than They Are Earning

---

**Robots got much smarter in the past two years. They have not yet become a big business, except in a few places most people overlook.**

You have probably seen the videos: a humanoid robot folding laundry, loading a dishwasher, or doing a backflip. They are real, and they show genuine progress. But I build these systems, and I can tell you what the videos rarely show: how many tries it took, whether a person was secretly steering, and how often the robot needs help on an ordinary Tuesday.

This column explains what is actually happening in "embodied AI" — AI with a body — in plain language. What works today, what is still hard, who is winning, and what it means for jobs, homes and society.

## What embodied AI is

**Embodied AI is AI that can see, move and touch things in the real world.** ChatGPT-style AI lives on a screen and produces words. Embodied AI lives in a machine and produces actions.

Think of the difference between a cookbook and a cook. A cookbook knows every recipe, but it cannot crack an egg. A cook has to deal with a slippery shell, a hot pan and a dog underfoot. Embodied AI is the cook.

Every such machine runs the same loop, many times a second:

1. **Sense** — cameras, touch sensors and motion sensors take in the world.
2. **Decide** — the AI works out what is going on and what to do next.
3. **Act** — motors move wheels, legs, arms or fingers.
4. **Repeat** — the action changes the world, so the robot must look again.

The family is much bigger than humanoid robots. It includes self-driving cars, warehouse robots that carry shelves, factory arms, delivery drones, robot vacuums and surgical robots. Humanoids get the headlines, but they are the newest and least proven members.

There is an old puzzle in this field, called **Moravec's paradox**. Things that are hard for people, like chess, turned out to be easy for computers. Things a toddler does without thinking, like picking up a sock, turned out to be extremely hard. That puzzle still explains why AI could write essays years before it could fold a towel.

## Where it already works today

**The biggest embodied-AI successes are not humanoids. They are cars without drivers and robots that move shelves.**

**Robotaxis.** Waymo, owned by Google's parent Alphabet, gives fully driverless, paid rides in several US cities. It was doing over 400,000 paid rides a week in early 2026, and its co-CEO has publicly targeted more than 1 million a week by the end of 2026 ([Bloomberg](https://www.bloomberg.com/news/articles/2026-02-11/waymo-co-ceo-outlines-path-to-1-million-weekly-trips-in-2026)). China's Baidu runs a large robotaxi service too. This is the clearest proof that AI can safely drive a machine through a messy, unpredictable world, at scale, for money.

**Warehouse robots.** Amazon announced in mid-2025 that it had deployed its one-millionth robot across more than 300 facilities ([Automated Warehouse](https://www.automatedwarehouseonline.com/amazon-deploys-million-robots-launches-new-ai-foundation-model/)). Most are low, flat robots that slide under shelves and bring them to human pickers. They are not glamorous. They work every day.

**Humanoids.** Here the numbers are much smaller. Analyst firm Omdia counted about 13,000 humanoid robots shipped worldwide in 2025, mostly by Chinese makers, and many went to universities and labs rather than real jobs ([TechNode, citing Omdia](https://technode.com/2026/01/09/chinas-agibot-leads-global-humanoid-robot-shipments-in-2025-omdia-says/)). The best-documented paid work is by Agility Robotics, whose Digit robot moves plastic bins in warehouses. Agility reported more than 65,000 hours of operation across nine customer sites as of May 2026, in documents filed with US regulators ([SEC filing](https://www.sec.gov/Archives/edgar/data/2074973/000121390026071290/ea029548401ex99-1.htm)).

Why the gap? Robotaxis and warehouse robots each do one well-defined job in a controlled setting. Humanoids promise to do *anything*, anywhere. That promise is far harder to keep.

The robotaxi story is also a useful warning about timelines. Self-driving cars took roughly 15 years to go from early research contests (the US DARPA challenges of the mid-2000s) to a real paid service. The last few percent of reliability took most of that time. I expect humanoids to follow a similar path.

## What changed: robots got general-purpose brains

**Since about 2023, robots have started using the same kind of AI that powers chatbots — and that is the real breakthrough.**

Old robots were programmed line by line: move 30 cm left, close gripper, lift. Change the cup, and the program broke. New robots use what researchers call **vision-language-action models**. In plain terms, they are "see, read, do" brains. The robot looks through its cameras, reads an instruction like "put the dishes away", and outputs movements.

Because these brains start from AI that has already learned from the internet, they arrive knowing what a mug, a drawer or a sock is. They then learn movement from examples. The main ways robots learn today:

- **Copying people.** A human steers the robot remotely, like a puppeteer, and the robot learns from thousands of recordings.
- **Practising in simulation.** Robots train in realistic video-game worlds, where they can fall a million times at no cost. This is how robots learned to walk and run so well.
- **Learning from their own mistakes.** The newest systems improve from their real-world successes and failures, not just from human examples.
- **Watching video.** Researchers are trying to teach robots from ordinary videos of people doing chores.

The pace in 2026 has been fast. A few examples:

- **Physical Intelligence** (US startup) released π0.7 in April 2026. It claims the robot can combine skills learned separately to do tasks it was never shown, such as folding shirts on a new type of robot.
- **Google DeepMind** released Gemini Robotics 2 in July 2026, demonstrated controlling the whole body of Apptronik's Apollo humanoid ([Robotics & Automation News](https://roboticsandautomationnews.com/2026/07/31/google-deepmind-unveils-gemini-robotics-2-as-apptronik-humanoid-demonstrates-whole-body-ai/103802/)).
- **NVIDIA** gives away its GR00T robot brains for free, so other companies can build on them — a strategy often compared to Android for phones ([NVIDIA](https://investor.nvidia.com/news/press-release-details/2026/NVIDIA-and-Global-Robotics-Leaders-Take-Physical-AI-to-the-Real-World)).

One honest caveat: almost every one of these results was measured by the company that built the model, usually against its own earlier version. Nobody has yet independently re-run the tests. That does not mean the progress is fake. It means we should treat headline numbers as claims, not facts.

## Why it's still hard

**The problem is no longer "can the robot do it once?" It is "can it do it ten thousand times without help?"**

**Reliability.** A robot that succeeds 95% of the time sounds impressive. But if it handles 300 items in a shift, that is about 15 failures a shift, and each one needs a person to walk over and fix it. The number that matters to a business is how often a human must step in, and how long the robot runs between breakdowns. Companies rarely publish either.

**Data.** Chatbots learned from most of the text on the internet. There is no internet of robot movements. Every hour of robot training data has to be recorded, usually by paying people to steer robots. That is why China now has dozens of dedicated robot "training centres", and why US firms run large data-collection warehouses.

**Hands and touch.** Walking on flat floors is now largely solved. Hands are not. Human hands have dense touch sensing and remarkable strength-to-size. Robot hands are expensive, fragile and mostly numb. Tasks like threading a cable, peeling a sticker or handling a wet plate remain very hard.

**The messy real world.** In my own work, many failures have nothing to do with intelligence. Sunlight through a window confuses a camera. A shiny surface looks like a hole. Sensors drift out of alignment over weeks. Rubber fingertips wear down and grip differently. Software updates break skills that worked yesterday. None of this shows up in a demo video.

**Safety.** A factory arm can simply freeze when something goes wrong. A two-legged robot cannot: if it stops, it falls, and a 60 kg machine falling near a person is dangerous. The standard engineering answer is to wrap the AI in a separate, simpler safety system that limits speed and force no matter what the AI decides. Today's safety rules were written for predictable machines, not for AI that learns, so certifying this is still unsettled.

**Cost and upkeep.** Humanoid batteries typically last a few hours. Robots need charging, spare parts, repairs and software care. Amazon has said its most advanced robotic warehouse needs about 30% more staff in maintenance, reliability and engineering roles ([Automated Warehouse](https://www.automatedwarehouseonline.com/amazon-deploys-million-robots-launches-new-ai-foundation-model/)). For a robot to pay off, it must beat the full cost of a human worker after all of this — and no Western humanoid company has yet published proof that it does.

## Who is winning: the US, China and the money

**China leads on building robots cheaply and in volume. The US leads on robot brains and on money raised. Neither has yet proven a profitable humanoid business at scale.**

**China** shipped most of the world's humanoids in 2025. Its makers, led by AgiBot and Unitree, sell simpler robots at far lower prices, backed by a deep local supply chain and strong government support. China's new Five-Year Plan for 2026–2030 names "embodied intelligence" as a priority industry ([MERICS](https://merics.org/en/report/embodied-ai-chinas-ambitious-path-transform-its-robotics-industry)). Beijing has also warned of overheating: with more than 150 humanoid companies, many will not survive.

**The US** has the best-funded companies and most of the leading AI models. Many of its startups are valued like big software companies, but very few have published how much they actually earn.

How much of the money is backed by hard evidence:

| Company | Country | Latest value (US$) | How solid is the number? |
| --- | --- | --- | --- |
| [Figure](https://finance.yahoo.com/news/figure-valued-39-billion-latest-131115237.html) | US | $39B (Sept 2025) | Private funding round; no revenue published |
| [Skild AI](https://www.businesswire.com/news/home/20260114335623/en/Skild-AI-Raises-$1.4B-Now-Valued-Over-$14B) | US | Over $14B (Jan 2026) | Private funding round, company-announced |
| [Unitree](https://www.cnbc.com/2026/08/06/chinese-humanoid-robot-maker-unitree-prices-ipo-at-9-billion-valuation.html) | China | About $9B at stock-market listing (Aug 2026) | Public listing with audited accounts — the most solid |
| [Agility Robotics](https://www.sec.gov/Archives/edgar/data/2074973/000121390026071290/ea029548401ex99-1.htm) | US | $2.5B (2026 listing deal) | Filed with US regulators; real customers disclosed |

Unitree matters most here, because its stock-market listing forced it to publish audited accounts. It showed real, profitable sales — mostly robots sold to researchers, developers and educators, not robots doing factory jobs.

**The hidden chokepoint is parts, not AI.** Robot joints rely on powerful magnets made from rare-earth metals, and China dominates their processing. When China tightened export controls on several rare earths and magnets in April 2025, Elon Musk said Tesla's Optimus robot production was affected ([Interesting Engineering](https://interestingengineering.com/culture/elon-musks-humanoid-robot-china-rare-earth-crackdown)). Chinese robot makers buy these parts at home without that hurdle. Whoever controls the motors, gears and magnets may matter as much as whoever has the smartest model.

## What it means for society

**The effects will be real but gradual: first on dull, heavy, hard-to-fill jobs, and on the privacy of anyone with a robot at home.**

**Jobs.** The first jobs robots take are moving boxes, feeding machines and repetitive inspection — work that is tiring and increasingly hard to staff. Robots also create jobs, as Amazon's maintenance figures show, but usually different jobs needing different skills, sometimes in different places. Research by economists Daron Acemoglu and Pascual Restrepo on US factory robots found real job and wage losses in the local areas most exposed to them. The lesson: the national average can look fine while specific towns and workers lose out. Today's humanoid numbers are still far too small to show up in national job data.

**Ageing populations.** This is the strongest reason governments care. Japan, South Korea, China and Singapore all face shrinking workforces and growing numbers of elderly people. Robots are pitched as part of the answer, especially in factories and, longer term, in elder care. Elder care is also where robots are least proven and where mistakes are least acceptable.

**Privacy at home.** A home robot has cameras and microphones and moves around your house. Some, like 1X's NEO, can be remotely steered by a company employee when the robot gets stuck ([Startup Fortune](https://startupfortune.com/1x-starts-delivering-its-20000-neo-home-robot-teleoperator-and-all/)). That means a stranger may, with permission, see inside your home. This is the most under-discussed consumer issue in the field.

**Security.** Robots controlled by AI can be tricked. Researchers at the University of Pennsylvania showed that carefully worded instructions could get AI-controlled robots, including a commercial robot dog, to carry out harmful actions ([RoboPAIR study](https://arxiv.org/html/2410.13691v1)). A hacked chatbot says bad things. A hacked robot can do them.

**Rules.** Regulation is catching up slowly. The EU's new Machinery Regulation, which covers AI-driven robots and their cybersecurity, applies from 20 January 2027 ([European Commission](https://transition-pathways.europa.eu/adv-man/legislation/eu-machinery-regulation-safety-baseline-ai-enabled-and-robotic-machinery)). There is still no finished international safety standard for humanoid robots. And it is unclear who is liable when an AI-driven robot hurts someone: the AI maker, the robot maker or the business using it.

**Military use.** Robots that can walk anywhere are useful to armies too. In 2022 several leading makers pledged not to weaponise their general-purpose robots, but that is a voluntary promise, not a law.

## How to read a robot video

**Before you are impressed by a robot video, ask five questions.** Companies rarely lie outright, but videos are easy to make look better than reality.

1. **Was a person steering it?** Look for the words "autonomous" or "teleoperated" (remote-controlled). If the video does not say, assume some human help.
2. **Is it sped up?** Many clips run at 2x to 10x speed. Real robot chores are often slow.
3. **Is it one take?** Cuts can hide failures, resets and retries.
4. **How many tries did it take?** One success out of twenty attempts makes a great video and a terrible product.
5. **Has the robot seen this place before?** A robot doing a task in the lab where it trained is far less impressive than doing it in a stranger's kitchen.

The best companies answer these questions on screen. When a company will not, that tells you something too.

## What comes next, and what most coverage misses

**Over the next two to five years, expect robots to win narrow, repetitive jobs in warehouses and factories. A truly useful general-purpose home robot is more likely a 2030s story.**

My rough expectations, with how confident I am:

- **Robot brains keep improving fast** (high confidence). The same AI wave that improved chatbots is now improving robots, and every major lab is investing.
- **Robotaxis spread to many more cities** (high confidence). This is where embodied AI will touch most people first.
- **Humanoids find paying work in warehouses and factories** (medium confidence), mostly moving bins and boxes, often behind safety barriers.
- **Home humanoids ship, but with a human on call** (medium confidence). Expect remote operators to quietly handle the hard parts for years.
- **Robots match human hands** (low confidence before 2030). The hardware is the bottleneck, not the software.

Forecasts in this field have a poor track record on timing. In April 2025, Musk said Tesla still planned to build thousands of Optimus robots that year; that did not happen at that scale. The pattern so far: optimists have been right about the direction and wrong about the dates, usually by years.

**What most coverage misses:**

- **Robots will mostly be rented, not bought.** Companies pay a monthly or hourly fee, like leasing a car. 1X offers its home robot for US$499 a month. That raises ordinary but important questions about who pays for repairs, upgrades and breakdowns.
- **Insurance has no history to go on.** Insurers have little data on accidents involving AI-driven robots, so expect high premiums and demands for detailed logs.
- **Upkeep is a hidden cost.** Charging, spare parts, repairs and remote operators rarely appear in the sales pitch.
- **Robots and software AI are merging.** The AI "agents" now handling office tasks are starting to plan robot tasks too. Robots will need the same controls as any employee or system: identity, permissions and an audit trail. Early experiments even let robots pay for their own charging, but that is still at the demo stage.
- **Small countries can still matter.** Singapore cannot match the US or China on scale. Instead it is positioning itself as a trusted testing ground. On 22 October 2026, its National Robotics Programme, with A\*STAR, NTU and Micron, launched the country's first national Embodied AI Challenge for manufacturing, with finals in March 2027 ([TNGlobal](https://technode.global/2026/10/22/singapore-launches-first-national-embodied-ai-challenge-to-accelerate-real-world-robotics-deployment-in-manufacturing/), [NRP](https://nrp.gov.sg/SGEAIchallenge/)). Independent, trusted testing is exactly what the field lacks.

## Can you build one yourself?

**Yes. For learning or a simple proof of concept, a small team or a classroom can build a working embodied-AI robot for a few hundred US dollars, using free software.** What you will not get on that budget is a robot reliable enough for real work. That is the point of a proof of concept: to learn what works, cheaply, before anyone spends serious money.

The reason this is now possible: open-source communities, led by Hugging Face's free LeRobot software, have published robot designs, training tools and ready-made robot brains that anyone can download.

### Pick a starting level

Prices below are approximate list prices in US dollars as of October 2026, before tax and shipping. They vary a lot by country and seller, so check locally.

| Level | Example | Approx. cost (US$) | Good for |
| --- | --- | --- | --- |
| 1. Simulation only | Free simulators such as MuJoCo, plus LeRobot | Free (needs a decent computer) | Learning the ideas with zero risk; schools with no hardware budget |
| 2. Desktop robot arm | [SO-101 open-source arm](https://techcrunch.com/2025/04/28/hugging-face-releases-a-3d-printed-robotic-arm-starting-at-100) | About $100 per arm self-built; about $220–500 for a ready kit or a two-arm teaching set | The best first project: teach a robot to pick up and sort objects by showing it |
| 3. Desktop social robot | [Reachy Mini](https://huggingface.co/blog/reachy-mini) | About $400–500 | Robots that see, listen, talk and react; good for classrooms and demos |
| 4. Robot dog | Unitree Go2 | Roughly $1,600 to $4,000+; programmable versions cost more | Walking, mapping and navigation projects |
| 5. Small humanoid | Unitree R1 or similar | Several thousand to tens of thousands | Only with a dedicated budget, space and supervision |

My advice: start at level 1 or 2. Most of what there is to learn about embodied AI fits on a desk.

### Practice guideline for a first project

1. **Pick one small, clear task.** "Pick up a block and put it in the box" is a good first goal. "Tidy the office" is not. Write down what counts as success before you start.
2. **Start in simulation.** Run the free simulator first. Mistakes cost nothing, and you will learn how the robot "thinks" before you touch hardware.
3. **Build or buy the robot.** A self-assembled desktop arm takes roughly a weekend. Ready-assembled kits save time and frustration, and are better for schools.
4. **Teach by showing.** With a two-arm teaching set, you move one arm by hand and the other copies you while cameras record. Dozens of short recordings of the same task are usually enough for a simple demo.
5. **Train a small robot brain.** Free, ready-made models can be fine-tuned on your recordings. A gaming-class computer or a few hours of rented cloud computing is typically enough for a desktop arm.
6. **Test honestly.** Run the task at least 20 times, move the objects around, change the lighting, and count successes and failures. Apply the five questions in "How to read a robot video" to your own results.
7. **Write down what you learned.** Note the success rate, what broke, and how often a person had to help. That record is the real output of a proof of concept.

### Stay safe and responsible

- **Physical safety.** Even small arms can pinch fingers and knock things over. Keep hands clear while the robot runs, know how to stop it instantly (unplug it if needed), and never leave a running robot unattended. Charge batteries on a non-flammable surface and follow the maker's instructions.
- **Supervise students.** For school use, an adult should supervise every powered session. Start with arms and desktop robots, not walking robots.
- **Cameras record people.** A robot's cameras and microphones collect personal data. Get consent from anyone who will be recorded, keep recordings stored locally, and delete what you do not need. Follow your local data-protection law, such as Singapore's PDPA.
- **Keep workplace pilots separate.** In a company, run the pilot away from customer areas and screens showing customer or payment data. Ask your IT and security team before connecting any robot to the company network, and keep it away from live systems.

### Set expectations

A desktop project will teach you more about embodied AI in a month than any amount of reading. It will also show you, first-hand, why the field's hardest problem is reliability. Your robot will probably succeed most of the time, fail in surprising ways, and need help more often than you expect. That is not failure. That is exactly what a proof of concept is for.

## The bottom line

**Embodied AI is real, it is improving quickly, and it is already earning money — just not mostly where the headlines point.** Driverless cars and warehouse robots are the quiet success. Humanoids are the exciting bet, with brains improving faster than bodies, budgets or safety rules.

The question to ask of any robot claim is simple: not "can it do this?", but "how often does a person still have to help?" When companies start publishing that number, the industry will have grown up.

## Sources

- [Bloomberg: Waymo co-CEO outlines path to 1 million weekly trips (Feb 2026)](https://www.bloomberg.com/news/articles/2026-02-11/waymo-co-ceo-outlines-path-to-1-million-weekly-trips-in-2026)
- [Insurance Journal / Bloomberg: Waymo at ~400,000 paid rides a week (Feb 2026)](https://amp.claimsjournal.com/news/national/2026/02/12/335668.htm)
- [Automated Warehouse: Amazon deploys 1 millionth robot, DeepFleet](https://www.automatedwarehouseonline.com/amazon-deploys-million-robots-launches-new-ai-foundation-model/)
- [TechNode: Omdia 2025 humanoid shipments (Jan 2026)](https://technode.com/2026/01/09/chinas-agibot-leads-global-humanoid-robot-shipments-in-2025-omdia-says/)
- [SEC: Churchill Capital Corp XI and Agility Robotics press release](https://www.sec.gov/Archives/edgar/data/2074973/000121390026071290/ea029548401ex99-1.htm)
- [Robotics & Automation News: Gemini Robotics 2 and Apptronik (Jul 2026)](https://roboticsandautomationnews.com/2026/07/31/google-deepmind-unveils-gemini-robotics-2-as-apptronik-humanoid-demonstrates-whole-body-ai/103802/)
- [NVIDIA: GTC 2026 physical AI announcements](https://investor.nvidia.com/news/press-release-details/2026/NVIDIA-and-Global-Robotics-Leaders-Take-Physical-AI-to-the-Real-World)
- [Reuters via Yahoo Finance: Figure valued at $39B (Sept 2025)](https://finance.yahoo.com/news/figure-valued-39-billion-latest-131115237.html)
- [Business Wire: Skild AI raises $1.4B, valued over $14B (Jan 2026)](https://www.businesswire.com/news/home/20260114335623/en/Skild-AI-Raises-$1.4B-Now-Valued-Over-$14B)
- [CNBC: Unitree prices IPO at $9B valuation (Aug 2026)](https://www.cnbc.com/2026/08/06/chinese-humanoid-robot-maker-unitree-prices-ipo-at-9-billion-valuation.html)
- [MERICS: Embodied AI — China's ambitious path (Apr 2026)](https://merics.org/en/report/embodied-ai-chinas-ambitious-path-transform-its-robotics-industry)
- [Interesting Engineering: China rare-earth controls and Optimus (Apr 2025)](https://interestingengineering.com/culture/elon-musks-humanoid-robot-china-rare-earth-crackdown)
- [Startup Fortune: 1X NEO deliveries and teleoperation](https://startupfortune.com/1x-starts-delivering-its-20000-neo-home-robot-teleoperator-and-all/)
- [Robey et al., Jailbreaking LLM-Controlled Robots (RoboPAIR), arXiv 2410.13691](https://arxiv.org/html/2410.13691v1)
- [European Commission: EU Machinery Regulation and AI-enabled machinery](https://transition-pathways.europa.eu/adv-man/legislation/eu-machinery-regulation-safety-baseline-ai-enabled-and-robotic-machinery)
- [TNGlobal: Singapore launches national Embodied AI Challenge (Oct 2026)](https://technode.global/2026/10/22/singapore-launches-first-national-embodied-ai-challenge-to-accelerate-real-world-robotics-deployment-in-manufacturing/)
- [National Robotics Programme: Singapore Embodied AI Challenge for Manufacturing](https://nrp.gov.sg/SGEAIchallenge/)
- Acemoglu, D. and Restrepo, P. (2020), "Robots and Jobs: Evidence from US Labor Markets", *Journal of Political Economy*.
- [TechCrunch: Hugging Face SO-101 arm, from about $100 (Apr 2025)](https://techcrunch.com/2025/04/28/hugging-face-releases-a-3d-printed-robotic-arm-starting-at-100)
- [CNX Software: SO-ARM101 two-arm kit pricing](https://www.cnx-software.com/?p=149841)
- [Hugging Face: Reachy Mini](https://huggingface.co/blog/reachy-mini)
- [Automated Warehouse: Unitree Go2 launch at $1,600](https://www.automatedwarehouseonline.com/unitree-launches-new-personal-quadruped-for-1600/)
- [Global Drone HQ: Unitree 2026 US price guide (dealer prices, Aug 2026)](https://globaldronehq.com/blogs/guides/unitree-robot-price-guide-2026)
