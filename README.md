**Task 1 --** <br><br>

**Python Installation:**<br><br>
<img width="940" height="81" alt="image" src="https://github.com/user-attachments/assets/0a6a0d52-409b-4000-8629-410c25551e51" /><br><br>
**Flutter Setup:**<br><br>
<img width="940" height="313" alt="image" src="https://github.com/user-attachments/assets/b7c6fc20-ac75-4b27-a10b-09a6f42fc005" /><br><br>
**MongoDB Ready:**<br><br>
<img width="940" height="319" alt="image" src="https://github.com/user-attachments/assets/979b13a0-7bbf-4e5e-8154-c119669d401c" /><br><br>
<img width="940" height="309" alt="image" src="https://github.com/user-attachments/assets/ee71523a-6680-4619-b469-f016db4026f0" /><br><br>
**Python Script:**<br><br>
<img width="940" height="69" alt="image" src="https://github.com/user-attachments/assets/2994a729-2e4a-4f77-a0ca-b1b2819e87ba" /><br><br>
**Flutter:**<br><br>
<img width="940" height="996" alt="image" src="https://github.com/user-attachments/assets/fa1f07c9-fb09-4fea-b8a7-e5db45bbdf5b" /><br><br>
## 🛠️ Setup Challenges Faced (Task 1)

During the Flutter environment setup, I faced a few challenges:

- **SDK Path Configuration:** Initially, Flutter commands didn’t run because the SDK path wasn’t added to the system environment variables.  
- **Android Toolchain Issues:** I had to manually install the missing `cmdline-tools` and accept licenses using `flutter doctor`.  
- **Android Toolchain Missing:** Flutter Doctor showed an error saying “cmdline-tools component is missing.” I had to install the command-line tools manually from the Android Studio SDK Manager.
- **Mongosh Command Issue:** The terminal did not recognize `mongosh` initially. I had to run it using `.\mongosh` or add its path to the system environment variables.  
- **MongoDB** was a bit difficult to install

After fixing these, Flutter Doctor showed all green checkmarks ✅ and I was able to run the app successfully on my phone. <br><br>
**Task 2 --**<br><br>
[**https://youtube.com/shorts/bNYTIoGNJbY?feature=share**](https://youtube.com/shorts/bNYTIoGNJbY?feature=share)<br><br>
<img width="613" height="1465" alt="image" src="https://github.com/user-attachments/assets/0649eb46-4a80-400f-ba99-af013eb6d588" /><br><br>
### 🧠 Brief Explanation: How I Handled the State Reset Requirement

I stored the counter value inside a **StatefulWidget**, so it only exists while the screen is open.  
When the screen is closed, Flutter removes the widget from memory, which also removes the counter value.  
When I open the screen again, the widget is created fresh, and the counter automatically starts again from **0**.

In short:  
- The counter value changes using `setState()` when I press the buttons.  
- When I leave the screen and come back, it resets because the widget is rebuilt from the start.
<br><br>
**Task 3 --**<br><br>
<img width="940" height="875" alt="image" src="https://github.com/user-attachments/assets/f5c4f1e5-ce56-4e6a-a06f-f940182288ef" /><br><br>
<img width="940" height="1131" alt="image" src="https://github.com/user-attachments/assets/939752ae-91e0-49ca-9272-36920ce412c4" /><br><br>
<img width="796" height="1453" alt="image" src="https://github.com/user-attachments/assets/368dc903-f259-4087-8102-43e2c6024e5e" /><br><br>
Embeddings help convert text (like video captions or descriptions) into numerical vectors that represent their meaning.  
When two pieces of content have similar embeddings, it means they talk about similar topics.  
Recommendation systems use this to show users more content that matches their interests — for example, if you watch a "football skills" reel, the system finds other reels with similar embeddings to recommend next.

