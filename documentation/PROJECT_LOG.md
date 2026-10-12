# Project Log

## 2026-09-03

### Starting point

This project currently consists of a basic Python menu program.

### Goal

I want to develop this into an educational cipher tool where users can select different cipher algorithms and encrypt or decrypt text.

### Goal for today

Today I plan to develop a Caesar cipher Python script where the user can choose to enter text to encrypt or enter already encrypted text and decrypt it.

Perhaps later I will also experiment with having `main.py` communicate with a separate Python file.

### ===============================================================================================

### Second Entry — 2026-09-04

I continued working on my Educational Cypher Tool and made some changes to the Caesar cipher. I realised there are two similar variants. The one I first created was the numeric shift variant. There was another letter key variant, which I managed to create today.

I gave the Caesar cipher and its two variants a dedicated folder, added a menu so the user can select between them, and reorganised my structure a little bit. `main.py` is now connected to `caesar_menu.py`, which prints out information about the Caesar cipher and its two variants. It then prompts the user to press enter to continue, after which it displays a menu that allows the user to select either of the two variants.

I also created the Atbash cipher using a similar structure to my Caesar cipher. I added an information section explaining how Atbash works and made it so that the same process can be used for both encryption and decryption.

I worked on code organisation by separating my code into different files and folders.

A big part of today's work was learning about **Python imports**. I also created a **terminal-clearing function**, put it into a `tools` folder, and moved the function into its own `terminal_cleaner.py` file. I then learned how to import the function into my cipher programs instead of having to write the same function in every file. Both of these ideas were new to me and I wasn't taught about them. I came up with the ideas, did some research, and taught myself how to implement them.

I also came across Python's `__pycache__` folders and `.pyc` files for the first time. I looked into what they were and learned that Python automatically creates these files when importing modules. I experimented with trying to organise where they were stored, but decided that it was better to let Python manage them normally and simply configure VS Code to hide them from the file explorer.

I also learned how to use a `.gitignore` file to prevent files such as Python cache files, VS Code settings, and environment files containing potentially sensitive information from being uploaded to GitHub.

Overall, this was useful because I learned quite a bit about **Python project organisation, imports, reusable modules, and how Python handles cached files**, most of which was completely new knowledge that I learned independently while working on the project.

### Future Goals

Since the three ciphers I currently have all fall into the group of **classical ciphers**, I would like to implement a few more classical ciphers before moving on to mechanical ciphers and eventually modern ciphers.

After finishing the classical ciphers, I was thinking about trying to build a simple webpage for the program. Instead of using terminal menus, buttons and other webpage elements would take over, making the program more interactive and user-friendly.

This would also give me an opportunity to learn more about web development and see how I could connect what I have already built in Python to a graphical interface.

### ===============================================================================================

### Third Entry — 2026-09-04

Another thing I considered was whether the classical cipher scripts should be divided further, since they currently handle multiple things. Aside from the cipher itself, they also contain the menu logic. However, the scripts are relatively simple and easy to read, and I frankly do not see much point in separating them further at this stage. I feel like doing so would create unnecessary chaos and make the project harder to work with if the code were spread across a sea of many smaller files. Since the code for each cipher is relatively small, I believe keeping one file for each cipher is the better alternative for now.

I also turned the upper- and lowercase alphabets into a separate `tool.py` script, which is then imported and used by the ciphers that need them. This allows me to reuse the same data without having to define it separately in every cipher script.

I then wrote scripts for the **Vigenère cipher, Affine cipher, Rail Fence cipher, and Columnar Transposition cipher**.

I now have six classical ciphers in the project, so I decided to store them all inside a dedicated `classical_ciphers` folder. `main.py` now leads to a `classical_ciphers_menu` within that folder, which then allows the user to select between the classical ciphers currently included in the program.

This also makes the project structure more organised and gives me a clearer foundation for adding other types of ciphers later.

### ===============================================================================================

### Fourth Entry — 2026-10-12

After some time away from actively developing this project, I continued working on it today. I have not abandoned this project or the other projects I am working on. There are simply other things in my life that sometimes require more of my attention.

Between university, studying and assignments, job hunting, helping at home, taking care of family members, and keeping up with my responsibilities, hobbies, relationships, church, volunteering, and other parts of my life, working on this project cannot always be my highest priority. Nevertheless, I still want to continue developing it because I am genuinely interested in cryptography and want to see how far I can take this project while learning along the way.

Today, I decided to reorganise the project further to make room for more advanced cryptographic methods. As the project was growing, I felt that keeping everything under the same structure would eventually become difficult to manage. I therefore separated the classical cryptography scripts into a dedicated `classical_cryptography` folder and introduced a new `modern_cryptography` folder. This gives the project a clearer structure and makes it easier to distinguish between classical ciphers and modern encryption methods.

I then started implementing **AES (Advanced Encryption Standard)** as part of my first cryptography lab. I implemented AES in CTR mode, using a password-derived key generated with PBKDF2-HMAC-SHA256. I also added HMAC-SHA256 to verify the integrity of the decrypted message and detect incorrect passwords or modified data. The implementation supports encrypting and decrypting files, and I added a menu that allows the user to test the functionality directly through the program.

After completing the AES implementation, I moved on to my second cryptography lab, which focused on **RSA and hybrid encryption**. I implemented RSA key generation with a password-protected private key and a corresponding public key. I then added digital signatures using RSA-PSS and SHA-256, allowing files to be signed and their signatures verified.

I also implemented hybrid encryption by combining AES-256 in CTR mode with RSA-OAEP. Instead of encrypting an entire file with RSA, the program generates a random AES session key to encrypt the file and then encrypts that session key using the RSA public key. This allowed me to explore how symmetric and asymmetric cryptography can work together.

Finally, I combined these components into an integrated workflow that signs and encrypts a file, then decrypts it and verifies its signature before accepting the recovered content. I tested the workflow successfully and modified the encrypted data to confirm that the program rejected the corrupted message. I also updated `.gitignore` to exclude the private RSA key and generated encryption artifacts from the repository.

This was an important step in the development of the project. I now have six classical ciphers alongside implementations of AES encryption, RSA key management, hybrid encryption, and digital signatures. More importantly, I have gained a better understanding of how these different cryptographic techniques complement each other and why encryption and integrity verification serve different purposes.

There are still improvements to make, particularly regarding authenticated encryption and separating the sender's signing key from the recipient's encryption key. However, I now have a functional foundation for exploring these improvements and expanding the project further.

### ============================================================================================