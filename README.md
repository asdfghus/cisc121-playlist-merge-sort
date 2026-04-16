
playlist-vibe-builder-merge-sort

# Merge Sort

## Demo video/gif/screenshot of test
base:
<img width="2858" height="1452" alt="image" src="https://github.com/user-attachments/assets/726c556d-989d-4c53-a54b-b5b582244c6a" />

https://github.com/asdfghus/cisc121-playlist-merge-sort/blob/main/base.png?raw=true

Duration:
1
<img width="2880" height="1546" alt="image" src="https://github.com/user-attachments/assets/8520935a-663f-40b8-92d6-e86e5f2f378a" />

https://github.com/asdfghus/cisc121-playlist-merge-sort/blob/main/duration1.png?raw=true
2
<img width="2740" height="642" alt="image" src="https://github.com/user-attachments/assets/f25a7816-1be3-498c-adae-b318c26fed6b" />

https://github.com/asdfghus/cisc121-playlist-merge-sort/blob/main/duration2.png?raw=true

Energy:
1
<img width="2876" height="1558" alt="image" src="https://github.com/user-attachments/assets/04ad2d73-3407-4b5f-9f2a-00fce2169570" />

https://github.com/asdfghus/cisc121-playlist-merge-sort/blob/main/energy1.png?raw=true
2
<img width="2880" height="972" alt="image" src="https://github.com/user-attachments/assets/0057db85-78ba-432f-ac38-8d43e31f2c59" />

https://github.com/asdfghus/cisc121-playlist-merge-sort/blob/main/energy2.png?raw=true

## Problem Breakdown & Computational Thinking

### Problem Description
This project demonstrates how Merge Sort can be used to organize a playlist of songs.  
Each song has:
- a title  
- an artist  
- an energy score  
- a duration  

The user selects a sorting key (energy or duration), and the app visually shows how Merge Sort compares and merges songs step-by-step.  
The goal is to help users understand how Merge Sort works while also solving a real-world style problem: organizing a playlist based on different attributes.

---
### Flowchart

Start
  User opens the app
    -User selects sorting key (energy or duration)
      -App begins Merge Sort
        -Split playlist into two halves
          -Recursively split each half until single items remain
        -Begin merging phase
          -Compare first items of each half
            -Take the smaller value based on chosen key
            -Add comparison to step log
          -Continue comparing until one half is empty
        -Append remaining items
      -Merged list returned
    -Display:
      -Original playlist
      -Sorted playlist
      -Step-by-step Merge Sort log
End



---
### Computational Thinking

#### **Decomposition**
- Break playlist into smaller sublists  
- Recursively sort each half  
- Merge sorted halves  
- Display steps to the user  

#### **Pattern Recognition**
- Repeated splitting  
- Repeated comparisons  
- Repeated merging  
- Same structure at every recursion level  

#### **Abstraction**
- Show only:
- comparisons  
- chosen elements  
- merged sublists  
- Hide recursion details  

#### **Algorithm Design**
- **Input:** playlist + sorting key  
- **Process:** Merge Sort with step logging  
- **Output:** sorted playlist + visual step log  
- Gradio UI handles user interaction  

---


## Steps to Run

### Run on Hugging Face
1. Open my Hugging Face Space:  
   **<YOUR HUGGING FACE LINK>**
2. Choose a sorting key (energy or duration)
3. Click **Sort Playlist**
4. View:
   - the original playlist  
   - the sorted playlist  
   - the Merge Sort step-by-step log  

## Hugging Face Link
https://huggingface.co/spaces/saefwdh/playlist-merge-sort-AyaanJalal

## Author & AI Acknowledgment
Created by **Ayaan Jalal**.  
Microsoft Copilot was used to help plan, structure, and explain parts of this project, as well as a search engine partner at level 3 A.I. Usage.


