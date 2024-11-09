import streamlit as st

# Title of the app
st.title("Cybersecurity Adventure Bot")

# Greet the user
st.header("Hello, Future Cyber Hero! 👑👑👑")
st.write("""
Welcome to your Cybersecurity Adventure! 🦸‍♂️🦸‍♀️
Let's learn about some important terms that will help you stay safe online! 
Ready? Let’s go!
""")

# Ask for user input
name = st.text_input("What's your name, hero?")
age = st.number_input("How old are you?", min_value=5, max_value=100, step=1)

# Ask about staying safe online
safe_online = st.radio("What do you think staying safe online means?", 
                       ("Not sharing personal information", 
                        "Only visiting trusted websites", 
                        "Using strong passwords"))

# Ask if they want to be a Cyber Hero Professional
wanna_be_hero = st.radio("Would you like to become a Cyber Hero Professional?", 
                         ("Yes, definitely!", "Maybe, I’m interested", "Not sure yet"))

# Show advice based on responses
if wanna_be_hero == "Yes, definitely!":
    st.write("That’s awesome, Cyber Hero! 💪 Your adventure starts here, and with every lesson, you’ll get one step closer to becoming a pro!")
elif wanna_be_hero == "Maybe, I’m interested":
    st.write("That’s a great start! Keep learning... and you might just become a Cyber Hero one day! 😉")
else:
    st.write("That's okay! Stay safe online and who knows, maybe one day you'll be ready to join the Cyber Hero league! 👑")

# Print the collected information for fun
st.write(f"Nice to meet you, {name}!")
st.write(f"You're {age} years old and it looks like you think staying safe online means: {safe_online}.")

# Basic questions and explanations
questions = {
    "What is Cybersecurity?": """
    Cybersecurity is all about protecting our computers, phones and all the information we use online. Imagine you have a house. Your house needs locks and alarms to keep bad people out, right? Well, the same thing happens with your devices! Cybersecurity is like your personal security guard for your computer or phone. It keeps all your private information safe from hackers and other online bad guys! 🛡️
    """,
    "What is a Virus?": """
    A virus is like a sneaky bug that gets inside your computer or phone without you knowing. Once it's inside, it can start causing trouble, like stealing your information or making your device slow. Just like how we get sick from germs, your device can get 'sick' from a virus. That's why you need antivirus software to catch these bugs and keep your device healthy! 🦠
    """,
    "What is a Firewall?": """
    Think of a firewall like a super strong wall around your house. It helps keep the bad guys out! A firewall checks every piece of data that tries to come into your computer or phone and makes sure it's safe. If it's not, it stops it from coming in! 🔥
    """,
    "What is a Password?": """
    A password is like a secret key that lets you into your personal accounts, like your email or games. If someone else finds your key, they could steal your stuff. So, it's super important to make your password strong and keep it secret! You should never share your password with anyone, not even your best friend! 🔑
    """,
    "What is Two-Factor Authentication (2FA)?": """
    Two-Factor Authentication (2FA) is like adding a second lock to your door. After you enter your password, 2FA asks for something else, like a code sent to your phone. This extra step makes it harder for bad guys to break into your account. It's like having two keys instead of just one! 🔐
    """,
    "What is Phishing?": """
    Phishing is when someone tries to trick you into giving them your personal information, like your password or credit card number. They do this by pretending to be someone you trust, like a friend or a website you visit. It’s like a fake treasure chest that looks shiny, but it’s actually empty and full of traps! 🐟
    """,
    "What is Malware?": """
    Malware is a bad software that gets inside your device and causes harm. It could slow down your computer, steal your info, or even break it! Imagine it like a little monster that hides inside your computer and causes trouble. You need good antivirus software to fight off malware! 💻👹
    """,
    "What is Encryption?": """
    Encryption is like putting your secret messages inside a locked box that only you and your friend can open. When you send a message, encryption makes sure no one can read it except the person you're sending it to. It's like sending a letter in a secret code! 🔒
    """,
    "What is a VPN (Virtual Private Network)?": """
    When you're in a public place like a café using free Wi-Fi, a VPN helps protect your privacy. It’s like putting on an invisibility cloak, so no one can see what you're doing online. A VPN keeps your personal information safe and makes sure no one can snoop on your online activities! 🕵️‍♂️🖥️
    """,
    "What is Hacking?": """
    Hacking is when someone tries to break into your computer or online accounts without permission. Hackers can steal your information or even control your device! It’s like a thief sneaking into your house and taking your stuff. That's why you need strong passwords and security to protect yourself from hackers! 💻🚨
    """,
    "What is a Spyware?": """
    Spyware is like a secret agent that sneaks into your computer and watches everything you do. It can steal your passwords, track your activities, and send the information to bad people. It's a sneaky villain, and you need antivirus software to stop it from spying on you! 🕵️‍♀️
    """,
    "What is a Trojan Horse?": """
    A Trojan Horse is like a gift that's actually a trap! It looks safe, but inside it hides something dangerous. Once you open it, it can start harming your computer, like stealing your data or installing malware. Never open files or links from strangers—always check before you click! 🎁👀
    """,
    "What is a Botnet?": """
    A botnet is a network of computers controlled by a hacker. Imagine a bunch of robots working together to do bad things like attack websites or steal information. They might use your computer without you even knowing it! You need strong security to make sure your device isn’t part of a botnet. 🤖
    """,
    "What is Social Engineering?": """
    Social engineering is when someone tricks you into giving away personal information, like your password or phone number, by pretending to be someone you trust. It’s like a con artist trying to fool you into thinking they're your friend. Never trust someone asking for private info—stay smart! 🧠
    """,
    "What is Ransomware?": """
    Ransomware is a type of malware that locks your files and asks for money to unlock them. It's like a kidnapper that takes your toys and says you have to pay to get them back! Always back up your files so you can keep them safe even if ransomware attacks. 💰🔒
    """,
    "What is an IP Address?": """
    An IP address is like your home address on the internet. It helps websites and apps know where to send the information you ask for. But, just like a real address, it can be used to find out where you are, so it’s important to keep it private and secure! 🌍📍
    """,
    "What is a Cookie?": """
    A cookie is a small piece of information stored on your device when you visit a website. It helps remember things like your login info or preferences, so you don’t have to re-enter them every time. But, some cookies can track what you do online, so be careful! 🍪
    """,
    "What is a DDoS Attack?": """
    A DDoS (Distributed Denial of Service) attack is when hackers flood a website with so much traffic that it can’t work properly. It’s like a crowd blocking the entrance to your favorite store so no one can get in! Websites can protect themselves with special security measures to prevent these attacks. 🌐🚫
    """,
    "What is a Backdoor?": """
    A backdoor is a secret way into a computer or system that hackers use to get in without anyone knowing. It’s like a hidden door in your house that you didn’t know about, and bad people can sneak in anytime! Always make sure your systems are secure and don’t have any backdoors open. 🚪
    """,
    "What is Cryptography?": """
    Cryptography is like creating secret codes that only you and your friend can understand. It helps keep your messages private by turning them into unreadable text, and only people with the secret code (or key) can read it. It’s like writing a letter in a secret language only you know! 🔑🕵️‍♂️
    """,
    "What is a Digital Signature?": """
    A digital signature is like signing your name on a document, but in the digital world. It proves that the message or file you received really came from you and hasn’t been changed. It’s like stamping your seal on a letter to show it’s officially from you! 🖋️
    """,
    "What is a Bot?": """
    A bot is a program or software that automatically does tasks for you. Some bots are helpful, like a search engine, but some can be bad, like those used in a botnet to do harmful things. Think of them like little robots doing tasks on the internet for humans, but sometimes, they are up to no good! 🤖
    """,
    "What is an Antivirus?": """
    Antivirus software is like a superhero for your computer. It protects your device by finding and removing viruses and malware that try to attack. It’s like having a guard dog that barks and chases away any bad guys trying to get in! 🦸‍♀️🦠
    """,
    "What is an Encryption Key?": """
    An encryption key is like the special lock and key that only you can use to open a secret box. It turns your messages into codes, and without the key, no one can read them. It’s like keeping your secret safe under a password only you know! 🔐
    """,
    "What is a Man-in-the-Middle Attack?": """
    A Man-in-the-Middle (MITM) attack happens when someone secretly listens to or changes the messages between two people. It’s like a spy who sits between you and your friend, reading and possibly changing the things you say to each other without you knowing! 🕵️‍♂️
    """,
    "What is a Vulnerability?": """
    A vulnerability is like a crack in a wall where someone can break in. It's a weak spot in a computer system that hackers can use to get inside. That's why it’s important to fix these cracks to keep your system strong and secure! 🔨
    """,
    "What is an Access Control List (ACL)?": """
    An Access Control List (ACL) is like a list of people who are allowed or not allowed to enter a room. It helps control who can access certain parts of a computer system or network. If you're not on the list, you're locked out! 🚪
    """,
    "What is a Security Patch?": """
    A security patch is like fixing a hole in your wall. When hackers find weaknesses in a system, security patches are updates that fix those weaknesses. Always make sure to update your software to stay safe! 🔧
    """,
    "What is Zero-Day Attack?": """
    A zero-day attack is when hackers use a weakness in a program that nobody knows about yet. It’s like finding a secret door no one else knew existed. Since there’s no fix for it, it’s extra dangerous! 🕵️‍♀️
    """,
    "What is Penetration Testing?": """
    Penetration testing is like hiring someone to try and break into your house to find out where the weak spots are. It helps you find out what needs fixing so the bad guys can’t get in. This is done in a controlled way to keep things safe! 🏠🔐
    """,
    "What is a Honeypot?": """
    A honeypot is like a fake treasure chest set up to trap bad guys. It looks valuable, but when a hacker tries to steal it, they get caught. It’s a way to trick the hackers into focusing on the wrong target! 🍯🐝
    """,
    "What is a Rootkit?": """
    A rootkit is a sneaky program that hides inside your computer, making it hard to detect. It lets a hacker secretly control your device. It’s like having a secret villain inside your house, controlling everything without you knowing! 🏠👀
    """,
    "What is a Clickjacking?": """
    Clickjacking is like tricking you into clicking on something you didn’t mean to click. It’s when hackers hide something harmful under a harmless-looking button or link. Be careful where you click, or you might get tricked into doing something bad! 🖱️
    """,
    "What is an IP Spoofing?": """
    IP Spoofing is when a hacker pretends to be someone else by changing their IP address. It's like using a fake ID to sneak into a party. Hackers do this to hide their true identity and do bad things without getting caught! 🎭
    """,
    "What is a Keylogger?": """
    A keylogger is a sneaky program that records everything you type on your keyboard. It can steal your passwords and personal info without you knowing. It's like having someone secretly watch you type everything you do! ⌨️
    """,
    "What is a Security Token?": """
    A security token is like a special key that gives you access to your online accounts. It’s used to make sure that it's really you trying to log in, not a hacker pretending to be you. Think of it as a secret handshake that only you and the website know! 🔑🤝
    """,
    "What is a Phishing Email?": """
    A phishing email is a trick message that looks like it's from someone you trust, like a friend or a company. It tries to get you to give away your personal info, like passwords. Don’t fall for it—if the email seems weird, it probably is! 📨
    """,
    "What is Multi-Factor Authentication (MFA)?": """
    Multi-Factor Authentication (MFA) is like having two locks on your door. After you enter your password, MFA asks for something else, like a code sent to your phone, to make sure it’s really you. The more layers of security, the harder it is for bad guys to get in! 🛡️
    """,
    "What is a Brute-Force Attack?": """
    A brute-force attack is when a hacker tries every possible password until they find the right one. It’s like guessing the combination to a lock by trying every number. Strong passwords make this much harder for hackers! 🔐
    """,
    "What is an SSL Certificate?": """
    An SSL certificate is like a magic shield that protects information sent between websites and your computer. It makes sure that your passwords and credit card numbers stay safe when you’re shopping online or logging in. You’ll see a little padlock symbol in the URL bar when a website is secure! 🔒
    """,
    "What is a Cybersecurity Framework?": """
    A cybersecurity framework is like a set of rules and guidelines that help protect your system. It’s like a blueprint that helps you build a strong house to keep the bad guys out. These frameworks help companies stay secure online! 🏠🔐
    """,
    "What is Data Loss Prevention (DLP)?": """
    Data Loss Prevention (DLP) helps stop important information from being lost or stolen. It's like having a vault to store your secret information so no one can accidentally take it or break into it! 🔐💼
    """,
    "What is an Air Gap?": """
    An air gap is a security measure where a computer or system is not connected to the internet. It’s like having a safe that’s locked away in a secret room where no one can get to it. Air gaps keep sensitive data super safe from hackers! 🛡️
    """,
    "What is a Cyber Attack?": """
    A cyber attack is when hackers try to break into your system or steal your information. It's like someone trying to break into your house to steal your stuff. Cyber attacks can happen in many ways, like phishing, malware, or DDoS attacks. Stay protected! 🚨
    """,
    "What is Cloud Security?": """
    Cloud security protects the information stored on the internet, called ‘the cloud’. It’s like storing your treasures in a safe box in the sky. But just like any box, it needs a strong lock and key to keep it safe from hackers! ☁️🔒
    """,
    "What is Social Media Security?": """
    Social media security is about keeping your accounts and information safe on platforms like Instagram, Facebook, or TikTok. It’s like locking your diary so no one can read your private thoughts. Always use strong passwords and be careful what you share! 📱🔐
    """,
    "What is a Security Breach?": """
    A security breach happens when someone gets into your system without permission. It’s like someone breaking into your house and stealing your stuff. When this happens, you need to act fast to stop them and fix the problem! 🚨
    """,
    "What is an Insider Threat?": """
    An insider threat is when someone inside your organization, like an employee or friend, causes harm. It's like a spy in your group trying to steal information or break things from the inside. Be careful about who you trust! 🕵️‍♂️
    """,
    "What is a Data Breach?": """
    A data breach is when personal information like your name, password, or credit card number is stolen. It’s like someone finding your secret notebook and taking your private details without permission. Always keep your info safe! 🔒
    """,
    "What is an Endpoint?": """
    An endpoint is any device that connects to a network, like your computer, phone, or tablet. It's like the door to your house that hackers might try to sneak through. Make sure your devices have strong security to keep your home safe! 🚪🔐
    """,
    "What is a Cybersecurity Policy?": """
    A cybersecurity policy is a set of rules that helps people and organizations stay safe online. It’s like a rulebook for keeping everything secure. These rules help prevent cyber attacks and keep your digital world safe! 📚🛡️
    """,
    "What is the Dark Web?": """
    The dark web is a hidden part of the internet that’s not easy to find or access. It’s like a secret underground world where illegal activities can happen. Stay away from it, and stick to the safer, brighter side of the web! 🌑🕵️‍♀️
    """,
    "What is a Ransomware Attack?": """
    Ransomware is like a bad guy locking up your files and asking for money to unlock them. It's like a kidnapper holding your data hostage and demanding a ransom. Always back up your data so you don’t have to pay the ransom! 💰💻
    """,
    "What is Two-Factor Authentication (2FA)?": """
    Two-Factor Authentication (2FA) is like adding an extra lock to your door. After entering your password, you’ll need a second code, like a text message or app notification, to enter. This makes sure it’s really you trying to get in! 🔑🛡️
    """,
    "What is a Denial-of-Service (DoS) Attack?": """
    A Denial-of-Service (DoS) attack is like a flood of requests that crashes a website or service, making it unavailable to others. It’s like trying to open a door but too many people are pushing on it at once, blocking everyone out! 🚪🚫
    """,
    "What is Digital Forensics?": """
    Digital forensics is the process of investigating and analyzing digital devices (like computers, smartphones, or hard drives) to find evidence of criminal activity or security breaches. It involves recovering deleted data, analyzing logs, and studying patterns in data that can help solve cybercrimes or track down hackers. Imagine being a detective, but instead of finding fingerprints, you're finding clues hidden in computers.
    """,
    "What is Public Key Infrastructure (PKI)?": """
    Public Key Infrastructure (PKI) is a framework that uses pairs of cryptographic keys—a public key and a private key—to secure digital communications. It's like sending a secret message where only the person with the private key can open it. PKI is used for securing websites, email communication, and data transfer, and it ensures trust and privacy.
    """,
    "What is a Root Certificate?": """
    A root certificate is the top-level certificate in a public key infrastructure (PKI) system. It is issued by a trusted certificate authority and is used to verify the identity of other certificates in the system. It's like the ultimate seal of approval, saying "this website or file is legit." Without it, digital communications wouldn’t be as secure.
    """,
    "What is a Cryptographic Hash Function?": """
    A cryptographic hash function takes an input (like a file or password) and turns it into a fixed-size string of characters, typically a number or a unique value. It's designed to be a one-way process, so you can’t reverse it. This is useful for checking if a file has been altered or if someone’s password is correct without actually storing the password itself.
    """,
    "What is a Digital Signature?": """
    A digital signature is like an electronic fingerprint that verifies the authenticity of a digital message or document. It uses public key cryptography to ensure that a message or file hasn’t been altered and that the sender is who they say they are. It’s like signing a letter with a pen, but it’s done electronically to prove that it’s really from you.
    """,
    "What is a Man-in-the-Middle (MITM) Attack?": """
    A Man-in-the-Middle (MITM) attack happens when a hacker secretly intercepts and possibly alters communication between two parties who think they are directly communicating with each other. It’s like someone sneaking into your conversation and listening to your private words without you knowing. This type of attack can steal sensitive data like passwords and credit card numbers.
    """,
    "What is Data Loss Prevention (DLP)?": """
    Data Loss Prevention (DLP) is a strategy or tool used to prevent sensitive data from being accidentally or intentionally leaked, lost, or accessed by unauthorized people. It monitors and blocks attempts to move or share sensitive information like credit card numbers, social security numbers, or confidential business data.
    """,
    "What is a Honeypot?": """
    A honeypot is a decoy system or server set up to attract and trap hackers. The idea is to lure them into attacking a fake target so that security experts can learn how hackers work and defend real systems better. Think of it like setting up a fake treasure chest to catch thieves while protecting the real treasure.
    """,
    "What is a Keylogger?": """
    A keylogger is a type of malware that secretly records every key you press on your keyboard. Hackers use keyloggers to steal sensitive information, like passwords and credit card details, by monitoring your typing without you knowing. It’s like someone peeking over your shoulder and writing down everything you type.
    """,
    "What is a Vulnerability Scanner?": """
    A vulnerability scanner is a tool that automatically checks computer systems, websites, or networks for weaknesses or flaws that could be exploited by hackers. It’s like using a magnifying glass to find cracks in your wall, so you can fix them before they get worse.
    """,
    "What is a Security Information and Event Management (SIEM)?": """
    Security Information and Event Management (SIEM) is a system that collects and analyzes log data from across a network to identify suspicious activities or potential security threats. It’s like having a security guard that watches everything happening on a network and alerts you if something looks dangerous.
    """,
    "What is an Intrusion Detection System (IDS)?": """
    An Intrusion Detection System (IDS) is a tool that monitors network traffic for signs of potential security breaches or attacks. It helps to detect unauthorized access or unusual behavior and alerts security teams about possible threats. It's like a motion sensor that alerts you when someone tries to sneak into your house.
    """,
    "What is a Firewall?": """
    A firewall is a network security system that monitors and controls incoming and outgoing traffic to prevent unauthorized access. It acts like a barrier or filter, letting safe data in while blocking harmful data. It’s like a security guard who checks everyone trying to enter a building.
    """,
    "What is Ransomware?": """
    Ransomware is a type of malware that locks or encrypts your files, then demands payment (ransom) to unlock them. It’s like a hacker holding your files hostage until you pay for them to be released. This type of attack can cause significant damage to businesses and individuals if the ransom isn’t paid or the files can’t be restored.
    """,
    "What is an Advanced Persistent Threat (APT)?": """
    An Advanced Persistent Threat (APT) is a highly sophisticated, long-term cyberattack in which hackers infiltrate a network and remain undetected for an extended period of time. APTs are usually carried out by well-funded and organized groups, often for espionage or data theft. It's like a thief who sneaks into your house and hides there for months, stealing small things without you noticing.
    """,
    "What is a Zero-Day Vulnerability?": """
    A zero-day vulnerability is a flaw or weakness in software that’s unknown to the software developer or vendor. Hackers can exploit this vulnerability before a patch is available to fix it, making it a dangerous window of time for attacks. It’s called "zero-day" because the developers have zero days to fix it before it’s used by hackers.
    """,
    "What is a Phishing Attack?": """
    Phishing is when hackers trick people into revealing personal information, such as passwords or credit card numbers, by pretending to be a trustworthy entity, like a bank or service provider. It’s often done through fake emails, websites, or messages. Think of it like a scam artist pretending to be someone you trust to steal your money or information.
    """,
    "What is a Distributed Denial-of-Service (DDoS) Attack?": """
    A Distributed Denial-of-Service (DDoS) attack is when a large number of computers or devices are used to flood a website or server with traffic, making it impossible for legitimate users to access the site. It’s like thousands of people calling a phone line at once to block others from getting through.
    """,
    "What is a Trojan Horse in Cybersecurity?": """
    A Trojan Horse is a type of malware that pretends to be a legitimate software or file, but once it's opened, it causes harm to your system. It’s named after the ancient Greek story of a hidden army inside a wooden horse. Once it’s inside, it can steal your data, crash your system, or create a backdoor for hackers.
    """,
    "What is Cryptojacking?": """
    Cryptojacking is when hackers secretly use your computer or device to mine cryptocurrency for themselves without your permission. This makes your device work harder, causing it to slow down or overheat. It’s like someone using your phone’s battery to make money for themselves while you don’t get anything in return.
    """,
    "What is a Backdoor in Cybersecurity?": """
    A backdoor is a secret way for hackers to access your system or network without being detected. It’s like leaving a hidden door in your house that you can use to enter anytime without anyone noticing. Backdoors are often used by hackers to maintain control of a compromised system.
    """,
    "What is Social Engineering?": """
    Social engineering is when hackers manipulate people into revealing sensitive information, such as passwords or security answers, by exploiting trust or emotions. It’s like a con artist convincing someone to give away secrets by pretending to be their friend.
    """,
    "What is Multi-Factor Authentication (MFA)?": """
    Multi-Factor Authentication (MFA) is a security process that requires more than just a password to verify your identity. It usually combines something you know (like a password), something you have (like a phone or security token), and something you are (like your fingerprint or face). It adds extra layers of security to make it harder for hackers to access your accounts.
    """,
    "What is the CIA Triad in Cybersecurity?": """
    The CIA Triad stands for Confidentiality, Integrity, and Availability, which are the three core principles of cybersecurity. Confidentiality ensures that only authorized users can access information. Integrity ensures that information is accurate and unaltered. Availability ensures that data and systems are accessible when needed. Together, these principles help protect systems and data from cyber threats.
    """,
    "What is Network Segmentation?": """
    Network segmentation is the practice of dividing a computer network into smaller, isolated sections to improve security. If one segment is breached, the damage can be contained without affecting the entire network. It’s like putting locks on different rooms in your house to limit how much a thief can steal if they break in.
    """,
    "What is a Proxy Server?": """
    A proxy server acts as a middleman between your device and the internet, hiding your real IP address and making requests on your behalf. It can help improve security by blocking malicious websites and allowing you to access content from different locations. Think of it like a shield that protects your identity while browsing the internet.
    """,
    "What is Cyber Threat Intelligence (CTI)?": """
    Cyber Threat Intelligence (CTI) is the collection and analysis of information about current and potential cyber threats, including tactics, techniques, and procedures (TTPs) used by attackers. It helps organizations anticipate and defend against cyberattacks. It’s like having a spy who provides information about enemy movements before they strike.
    """,
    "What is the Dark Web?": """
    The Dark Web is a part of the internet that is not indexed by regular search engines. It’s often used for illegal activities, like selling stolen data or illegal goods. It requires special software, like Tor, to access. It’s like a hidden part of the internet where shady dealings happen away from the public eye.
    """,
    "What is a Botnet?": """
    A botnet is a network of infected devices, like computers or smartphones, that are controlled by a hacker. The hacker can use these devices to launch attacks or send spam without the owners knowing. It’s like a hacker turning innocent devices into their army of robots to do their bidding.
    """,
    "What is a Worm in Cybersecurity?": """
    A worm is a type of malware that spreads automatically across networks, often causing damage by consuming bandwidth and corrupting files. Unlike viruses, worms don’t need a host to spread; they just replicate themselves. It’s like a virus that moves on its own and infects other devices without anyone having to open a file.
    """,
    "What is a SQL Injection Attack?": """
    SQL Injection is when a hacker sends malicious code to a website’s database by exploiting vulnerabilities in its code. The hacker can then steal, delete, or modify data. It’s like sending a hacker note to a store’s database, asking it to give you sensitive information, like customer data.
    """,
    "What is a Security Token?": """
    A security token is a physical or digital object used to authenticate a user’s identity. It’s often used in two-factor authentication (2FA) systems. Think of it like a keycard or an app that generates special codes to make sure you’re really who you say you are.
    """,
    "What is DNS Spoofing?": """
    DNS Spoofing is when a hacker tricks your device into visiting a fake website instead of the real one. They do this by changing the DNS (Domain Name System) records to send you to a malicious site. It’s like a hacker giving you a fake map, leading you to the wrong location while you think you’re going to the right place.
    """,
    "What is a Logic Bomb?": """
    A logic bomb is a piece of malicious code that’s triggered by a specific event or condition, like a date or time. When the event happens, the logic bomb activates and causes damage. It’s like a timer bomb that sits quietly until it’s triggered to explode and cause harm.
    """,
    "What is Endpoint Security?": """
    Endpoint security refers to protecting devices like computers, smartphones, and tablets that connect to a network. These devices can be vulnerable points of entry for hackers, so they need special software to stay secure. It’s like having security guards at every door in your house to prevent intruders from getting in.
    """,
    "What is a DDoS Attack?": """
    A Distributed Denial-of-Service (DDoS) attack is when many devices are used to flood a website with fake traffic, making it crash or become unavailable to real users. It’s like a huge crowd of people blocking the entrance to a building, preventing anyone else from getting inside.
    """,
    "What is a Backdoor Trojan?": """
    A backdoor Trojan is a type of malware that gives hackers secret access to your system, even after the malware is detected and removed. It's like a hidden door that the hacker can use to sneak back into your house without you noticing.
    """,
    "What is a Phishing Scam?": """
    A phishing scam is when hackers trick people into revealing their sensitive information, like passwords or credit card numbers, by pretending to be a trustworthy source. It’s like a con artist sending you a fake email pretending to be your bank, trying to get you to hand over your money.
    """,
    "What is a Cryptographic Key?": """
    A cryptographic key is a piece of information used in encryption to secure data. It’s like a secret code that only certain people can use to lock or unlock information. Without the key, it’s impossible to decrypt the data.
    """,
    "What is an SSL/TLS Certificate?": """
    SSL (Secure Sockets Layer) and TLS (Transport Layer Security) are protocols that encrypt data between your browser and a website. Websites with an SSL/TLS certificate are secure because they use encryption to protect your data from being intercepted by hackers. It’s like a locked box that only you and the website can open.
    """,
    "What is Two-Factor Authentication (2FA)?": """
    Two-Factor Authentication (2FA) adds an extra layer of security to your accounts. It requires you to enter both your password and a second verification, like a code sent to your phone. It’s like having two locks on your door—just your password isn't enough to get in; you need that extra key to unlock it.
    """,
    "What is a Reverse Engineering Attack?": """
    Reverse engineering is when hackers dissect a piece of software or hardware to understand how it works and exploit any weaknesses. It’s like taking apart a locked box to figure out the combination or how to break in.
    """,
    "What is a Key Exchange Algorithm?": """
    A key exchange algorithm is a method used to securely exchange cryptographic keys over a public channel. This ensures that only the intended parties can access the information. It’s like securely sharing a secret code without anyone else being able to overhear.
    """,
    "What is a Zero-Day Attack?": """
    A Zero-Day attack exploits a vulnerability in software that is unknown to the vendor. Hackers take advantage of this gap before the developers can release a fix. It’s like finding a crack in the door that no one else knows about and using it to break into a house before anyone can repair it.
    """,
    "What is Penetration Testing?": """
    Penetration testing, or ethical hacking, is when security professionals intentionally try to break into systems to find weaknesses before hackers do. It’s like hiring a hacker to test how strong your locks are by attempting to break into your house in a controlled way.
    """,
    "What is a Cipher?": """
    A cipher is an algorithm used to encrypt or decrypt data. It scrambles the data into a format that’s unreadable without the correct key. It’s like using a secret code to write messages that only someone with the key can decode.
    """,
    "What is a Man-in-the-Browser Attack?": """
    A Man-in-the-Browser (MitB) attack happens when malware infects your web browser and intercepts your online transactions or actions. It’s like a hacker secretly controlling your web browser and altering things without you realizing it.
    """,
    "What is Malware as a Service (MaaS)?": """
    Malware as a Service (MaaS) is a business model where hackers sell or lease malware to other criminals. It allows people without technical skills to launch cyberattacks. It’s like buying a weapon from a store and using it to rob a bank, but without needing to know how to build the weapon.
    """,
    "What is an Internet of Things (IoT) Security Vulnerability?": """
    IoT security vulnerabilities are weaknesses found in devices that are connected to the internet, like smart TVs or fridges. Hackers can exploit these vulnerabilities to gain access to private networks. It’s like leaving a window open in your house for burglars to sneak in through, even if the front door is locked.
    """,
    "What is a Rootkit?": """
    A rootkit is a type of malware that hides itself deep within a computer's operating system, making it difficult to detect. It allows hackers to maintain control over the system while hiding their actions. It’s like an intruder sneaking into your house and hiding behind the walls so you can’t see them.
    """,
    "What is a Botnet Command-and-Control (C&C) Server?": """
    A Botnet Command-and-Control (C&C) server is a central server used by hackers to send commands to the infected devices in their botnet. It’s like a puppet master controlling a group of robots, telling them what to do.
    """,
    "What is Data Encryption?": """
    Data encryption is the process of converting data into an unreadable format to prevent unauthorized access. Only someone with the encryption key can decrypt it. It’s like locking your information in a box that only you have the key to open.
    """,
    "What is a Cloud Security Breach?": """
    A cloud security breach is when unauthorized individuals gain access to data stored in cloud services. Cloud services are convenient but can be vulnerable if not properly secured. It’s like someone breaking into a secure online storage system and stealing your files.
    """,
    "What is the Principle of Least Privilege?": """
    The Principle of Least Privilege is a security concept that states users and programs should only have access to the resources they need to perform their job. Limiting access minimizes the potential for damage if an account is compromised. It’s like giving people keys only to the rooms they need to enter in your house, instead of giving them access to every room.
    """,
    "What is a Digital Footprint?": """
    A digital footprint is the trail of data you leave behind when you use the internet, including your social media activity, websites you visit, and searches you make. It’s like the tracks you leave in the sand that show where you've been online.
    """,
    "What is Threat Hunting?": """
    Threat hunting is a proactive approach to identifying potential cyber threats by actively searching for signs of suspicious activity in your network. It's like being a detective, searching for clues to prevent a crime before it happens.
    """,
    "What is a Buffer Overflow?": """
    A buffer overflow occurs when more data is written to a buffer (a temporary storage area) than it can hold, causing the overflowed data to overwrite adjacent memory. Hackers exploit buffer overflows to execute malicious code. It’s like pouring too much water into a glass, causing it to spill over and flood the table.
    """,
    "What is an Exploit Kit?": """
    An exploit kit is a toolkit used by hackers to automate the process of exploiting vulnerabilities in a system. It’s like a toolkit designed for breaking into systems without needing to know much about hacking, making it easier for criminals to launch attacks.
    """,
}

# Show explanations with expanders
for term, explanation in questions.items():
    with st.expander(term):
        st.write(explanation)

import streamlit as st

# Sample questions for the quiz
def get_quiz_questions():
    return [
        {"question": "What is Phishing?", "options": ["A. A type of malware", "B. A method of stealing personal information", "C. A type of firewall"], "answer": "B"},
        {"question": "What is Malware?", "options": ["A. A type of firewall", "B. Software designed to damage or exploit a device", "C. A type of virus"], "answer": "B"},
        {"question": "What does a Firewall do?", "options": ["A. Monitor network traffic", "B. Damage your system", "C. Encrypt your data"], "answer": "A"},
        {"question": "What is Ransomware?", "options": ["A. Software that demands payment to unlock files", "B. A method of hacking", "C. A type of virus"], "answer": "A"},
        {"question": "What is an Exploit Kit?", "options": ["A. A toolkit to defend systems", "B. A toolkit for hacking systems", "C. A firewall software"], "answer": "B"},
        {"question": "What is a Trojan?", "options": ["A. A type of malware that hides inside a legitimate program", "B. A type of antivirus software", "C. A type of computer hardware"], "answer": "A"},
        {"question": "What does SSL stand for?", "options": ["A. Secure Software Layer", "B. Secure Sockets Layer", "C. Secure System Layer"], "answer": "B"},
        {"question": "What is Two-Factor Authentication?", "options": ["A. A password system", "B. A method of securing online accounts with two forms of verification", "C. A type of encryption"], "answer": "B"},
        {"question": "What is a DDOS attack?", "options": ["A. A type of encryption", "B. A distributed denial of service attack", "C. A password attack"], "answer": "B"},
        {"question": "What is a Botnet?", "options": ["A. A network of computers used for attacks", "B. A type of malware", "C. A type of firewall"], "answer": "A"},
        {"question": "What is a VPN?", "options": ["A. Virtual Protection Network", "B. Virtual Private Network", "C. Virtual Public Network"], "answer": "B"},
        {"question": "What is Social Engineering?", "options": ["A. A technique used to manipulate individuals into revealing confidential information", "B. A type of virus", "C. A security protocol"], "answer": "A"},
        {"question": "What is Encryption?", "options": ["A. The process of securing data by converting it into a code", "B. The process of deleting data", "C. The process of improving internet speeds"], "answer": "A"},
        {"question": "What is a Vulnerability?", "options": ["A. A weakness that could be exploited in a system", "B. A type of malware", "C. A password protection method"], "answer": "A"},
        {"question": "What is a Zero-Day Attack?", "options": ["A. An attack that happens before a patch or fix is available", "B. An attack using outdated software", "C. An attack that occurs after a patch has been released"], "answer": "A"},
        
    
    
        {"question": "What does 'phishing' mean?", "options": ["A. A method of stealing personal information", "B. A type of antivirus software", "C. A network security feature"], "answer": "A"},
        {"question": "What is 'malware'?", "options": ["A. Software that protects your computer", "B. Software that damages or exploits your computer", "C. Software that speeds up your computer"], "answer": "B"},
        {"question": "What does a firewall do?", "options": ["A. Helps protect your data by blocking harmful traffic", "B. Makes your internet connection faster", "C. Protects your email from spam"], "answer": "A"},
        {"question": "What is 'ransomware'?", "options": ["A. Software that locks your computer until you pay", "B. Software that helps protect your computer", "C. A way to speed up your internet connection"], "answer": "A"},
        {"question": "What is a 'Trojan' in cybersecurity?", "options": ["A. A harmless program", "B. A malicious program that disguises itself as useful", "C. A firewall program"], "answer": "B"},
        {"question": "What is SSL used for?", "options": ["A. To make websites secure", "B. To create new passwords", "C. To block hackers from accessing websites"], "answer": "A"},
        {"question": "What is two-factor authentication?", "options": ["A. A method to protect your online accounts using two steps", "B. A type of malware", "C. A program to delete your old passwords"], "answer": "A"},
        {"question": "What does a DDoS attack do?", "options": ["A. Crashes a website by overwhelming it with traffic", "B. Helps protect your data", "C. Makes websites faster"], "answer": "A"},
        {"question": "What is a botnet?", "options": ["A. A network of infected computers controlled by hackers", "B. A software that speeds up your computer", "C. A firewall that blocks viruses"], "answer": "A"},
        {"question": "What does a VPN do?", "options": ["A. Protects your identity and encrypts your internet traffic", "B. Protects your email", "C. Speeds up your internet connection"], "answer": "A"},
        {"question": "What is 'social engineering'?", "options": ["A. A method of tricking people into revealing personal information", "B. A type of password", "C. A way to create strong security passwords"], "answer": "A"},
        {"question": "What is encryption?", "options": ["A. Turning data into a code to keep it safe", "B. The process of deleting old data", "C. The process of organizing your files"], "answer": "A"},
        {"question": "What is a vulnerability in a system?", "options": ["A. A weakness that could be exploited by hackers", "B. A tool to make your computer faster", "C. A type of antivirus"], "answer": "A"},
        {"question": "What is a zero-day attack?", "options": ["A. An attack that takes advantage of a flaw before a fix is available", "B. An attack using an outdated version of a program", "C. A tool to protect your computer"], "answer": "A"},
        {"question": "What is phishing?", "options": ["A. A way to trick people into giving personal information", "B. A method of securing passwords", "C. A type of firewall program"], "answer": "A"},
        {"question": "What is the best way to avoid phishing emails?", "options": ["A. Don’t click on links from strangers", "B. Reply to emails from unknown senders", "C. Open every email you receive"], "answer": "A"},
        {"question": "What is a secure website?", "options": ["A. A website with 'https' in the URL and a lock symbol", "B. A website that is only accessible from your computer", "C. A website that has a lot of advertisements"], "answer": "A"},
        {"question": "What is the purpose of a password manager?", "options": ["A. To store and generate secure passwords", "B. To block websites", "C. To speed up internet connections"], "answer": "A"},
        {"question": "What is the most common type of malware?", "options": ["A. Viruses", "B. Trojans", "C. Firewalls"], "answer": "A"},
        {"question": "Why should you update your software regularly?", "options": ["A. To fix security issues and protect against attacks", "B. To improve your internet speed", "C. To make your computer more colorful"], "answer": "A"},
        {"question": "What is 'phishing scam'?", "options": ["A. An attempt to steal personal information through fake emails or websites", "B. A type of malware", "C. A game to improve security skills"], "answer": "A"},
        {"question": "What is the purpose of an antivirus?", "options": ["A. To protect your computer from harmful software", "B. To delete personal files", "C. To create strong passwords"], "answer": "A"},
        {"question": "What should you do if you find a suspicious email?", "options": ["A. Do not click any links and report it", "B. Forward it to your friends", "C. Reply and ask for more details"], "answer": "A"},
        {"question": "What does 'https' stand for?", "options": ["A. Hyper Text Transfer Protocol Secure", "B. High-Tech Security Program", "C. Home Tool for Secure Passwords"], "answer": "A"},
        {"question": "What is 'spoofing' in cybersecurity?", "options": ["A. Pretending to be someone else to steal information", "B. A way to create strong passwords", "C. A method to improve internet speed"], "answer": "A"},
        {"question": "What is a hacker?", "options": ["A. A person who breaks into computer systems to steal information", "B. A person who helps protect systems", "C. A tool to speed up your computer"], "answer": "A"},
        {"question": "What is a 'data breach'?", "options": ["A. When sensitive data is exposed or stolen", "B. A tool to organize data", "C. A method of backing up data"], "answer": "A"},
        {"question": "What should you do if your password is compromised?", "options": ["A. Change your password immediately", "B. Ignore it", "C. Share it with your friends"], "answer": "A"},
        {"question": "What is a VPN used for?", "options": ["A. Protecting your identity and encrypting internet traffic", "B. Making your computer run faster", "C. Helping you play online games"], "answer": "A"},
        {"question": "What is 'adware'?", "options": ["A. Software that displays ads", "B. Software that protects against viruses", "C. A tool to improve security on websites"], "answer": "A"},
        {"question": "What is a 'cookie' on websites?", "options": ["A. Small pieces of data stored to remember user preferences", "B. A harmful software program", "C. A tool to block hackers"], "answer": "A"},
        {"question": "What is a 'patch' in cybersecurity?", "options": ["A. A fix for security vulnerabilities", "B. A new password", "C. A tool to delete old files"], "answer": "A"},
        {"question": "What is 'identity theft'?", "options": ["A. Stealing someone's personal information to commit fraud", "B. A way to improve your security", "C. A technique for creating strong passwords"], "answer": "A"},
        {"question": "What is 'spam' in cybersecurity?", "options": ["A. Unsolicited emails, usually with ads or scams", "B. A program that speeds up your computer", "C. A type of malware"], "answer": "A"},
        {"question": "What is the best way to create a strong password?", "options": ["A. Use a mix of letters, numbers, and symbols", "B. Use your name", "C. Use the same password for every account"], "answer": "A"},
        {"question": "What does 'pharming' do?", "options": ["A. Redirects users to fraudulent websites", "B. Speeds up your internet", "C. Creates strong passwords"], "answer": "A"},
        {"question": "What is a 'keylogger'?", "options": ["A. Software that tracks your keystrokes to steal information", "B. A type of antivirus", "C. A tool to make your computer faster"], "answer": "A"},
        {"question": "What is 'data encryption'?", "options": ["A. Converting data into a secure code", "B. A method to delete old files", "C. A type of firewall"], "answer": "A"},
        {"question": "What is 'clickjacking'?", "options": ["A. A method of tricking users into clicking on hidden links", "B. A type of password manager", "C. A tool for website protection"], "answer": "A"},
        {"question": "What is a 'trojan horse' virus?", "options": ["A. A type of malware disguised as a legitimate program", "B. A type of security tool", "C. A method of creating strong passwords"], "answer": "A"}
    ]


# Create a function to calculate the score for each group
def calculate_score(group_answers, questions):
    score = 0
    feedback = []
    for i, answer in enumerate(group_answers):
        correct_answer = questions[i]['answer']
        if answer.upper() == correct_answer:  # Make comparison case-insensitive
            feedback.append(f"Question {i+1}: Correct! 🎉")
            score += 1
        else:
            feedback.append(f"Question {i+1}: Wrong! The correct answer is '{correct_answer}'")
    return score, feedback

# Streamlit app layout
st.title("Cybersecurity Quiz - Group Challenge")

# Instructions
st.write("Form two groups and quiz each other on the terms you've learned!")

# Define tabs for each group
group1_name = st.text_input("Enter name for Group 1:")
group2_name = st.text_input("Enter name for Group 2:")

if group1_name and group2_name:
    # Create two columns for group members to input their names
    col1, col2 = st.columns(2)

    with col1:
        st.subheader(f"Enter members' names for {group1_name}:")
        group1_members = []
        for i in range(2):
            member_name = st.text_input(f"Member {i+1}", key=f"group1_member_{i}")
            if member_name:
                group1_members.append(member_name)

    with col2:
        st.subheader(f"Enter members' names for {group2_name}:")
        group2_members = []
        for i in range(2):
            member_name = st.text_input(f"Member {i+1}", key=f"group2_member_{i}")
            if member_name:
                group2_members.append(member_name)

    # Display the members' names
    st.write(f"Group 1: {group1_name} - Members: {', '.join(group1_members)}")
    st.write(f"Group 2: {group2_name} - Members: {', '.join(group2_members)}")

    # Get quiz questions
    questions = get_quiz_questions()

    # Store group answers
    group_answers = {group1_name: [], group2_name: []}

    # Show quiz to each group and collect answers
    for group_name in [group1_name, group2_name]:
        st.subheader(f"Quiz for {group_name}")
        group_responses = []

        # Loop through all questions
        for question in questions:
            answer = st.radio(f"{question['question']}", question['options'], key=f"{group_name}_{question['question']}")
            group_responses.append(answer.split(".")[0].strip())  # Capture only 'A', 'B', or 'C'

        # Save answers for each group
        group_answers[group_name] = group_responses

    # Button to show scores
    if st.button("Submit Answers"):
        st.header("Results")
        
        # Calculate and display results for both groups
        score_group1, feedback_group1 = calculate_score(group_answers[group1_name], questions)
        score_group2, feedback_group2 = calculate_score(group_answers[group2_name], questions)

        # Display scores and feedback
        st.write(f"{group1_name} scored: {score_group1}/{len(questions)}")
        for feedback in feedback_group1:
            st.write(feedback)
        
        st.write(f"{group2_name} scored: {score_group2}/{len(questions)}")
        for feedback in feedback_group2:
            st.write(feedback)

        # Determine the winner
        if score_group1 > score_group2:
            st.write(f"{group1_name} wins! 👑🎉")
        elif score_group2 > score_group1:
            st.write(f"{group2_name} wins! 👑🎉")
        else:
            st.write("It's a tie! Both groups are Cyber Heroes! 👑🎉")
