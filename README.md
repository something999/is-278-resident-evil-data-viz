# IS278 Final Project

## Contributors:

- **Matthew (matthewsmith788)**  
  I'm Matthew Smith. My role in the group involved cleaning and processing the scripts of Resident Evil 2, Resident Evil 3, and Resident Evil 2 Remake. I created word clouds of Leon and Claire from Resident Evil 2 and Resident Evil 2 Remake and heat maps based on MALLET analyses. I also assisted in mapping dialogue to proper character names in Resident Evil 3 Remake and Resident Evil 0.

- **Nichole (something999)**  
  I cleaned, standardized, and transformed scripts for all thirteen of the Resident Evil games, as well as created bar charts and pie charts highlighting historical trends in the series.

- **Amelia (abbarbee)**  
  I worked on initial cleaning of Resident Evil 4 and Resident Evil 5 using regex and Python, participated in MALLET exploration, and synthesized our narrative statement, environmental scan, and contribution statement.

- **Krystal (kreestalnavarro)**  
  I worked on initial cleaning of Resident Evil 6. I also participated in an exploration of verbs, dubbed action words, in video games. I am responsible for working on the code to parse the scripts of Resident Evil 2 and the Resident Evil 2 remake to create graphs comparing the number of verbs said by female vs. male characters and word count graphs. I also did the user analysis.

- **Qiqi (qqilinn)**  
  I worked on initial cleaning for Resident Evil 7 and 8, researched on different topic modeling tools and programs, and analyzed the scripts with Resident Evil 2 and its remake using LDA topic modeling in Python. I also arranged for our groups to meet with librarians in charge of the video games collection at UCLA library and Leigh Phan at the Data Science Center to discuss resources available at UCLA to develop our project.

---

This project is focused on female characters, both playable and non-playable, in the Resident Evil video game series. As a highly popular and long-running franchise, Resident Evil is uniquely suited to showcase changes in female characters’ roles over time, through remakes, and in reaction to cultural changes in both its native Japan and abroad. Resident Evil focuses on survival horror, a genre that typically explores unequal power dynamics (monster versus humans and human versus human). When considering this series, our team asked how we could best visualize the role of female characters in the Resident Evil series, as well as if those roles had changed significantly as the series progressed.

This project’s audience can be broadly described as gamers, or those who play video games. According to the Entertainment Software Association’s 2024 survey, over 190 million Americans play video games. ([ESA, 2024, 4](https://www.theesa.com/resources/essential-facts-about-the-us-video-game-industry/2024-data/)) Of these, 46% identify as female, 53% as male, and 1% identify as non-binary or decline to state. Other regions, like the Philippines with 63% female gamers, have a much higher rate of female gaming. ([Niko Partners, 2024](https://nikopartners.com/leveling-the-playing-field-for-women-in-gaming/)) The quantification of gamers being either male or female also leaves out the increasing number of gender-nonconforming gamers and does not account for the number of queer gamers either.

These distinctions are important to make. The heart of our project is to investigate female characters in Resident Evil; by investigating female characters, we are attempting to answer the question of whether or not female characters are represented in a way women want to see and interact with. It is difficult to find specific data on the number of female players vs. male players of Resident Evil. In some research, our team was able to find a survey on GameFAQs of Playstation 3 players. Of the 605 survey-takers, 69.92% were male and 30.08% were female – though this survey is 11 years old. ([GameFAQ](https://gamefaqs.gamespot.com/boards/605603-resident-evil-6/65100695?page=15)) Surveys like this also beg the question of who is more likely to be on a website like GameFAQs to see the survey in the first place.

There is no shortage of scholarship on women in video games, both involved in the games themselves and their creation. Our work intends to build on this scholarship by both focusing on one particular series, thus minimizing interference, and by visualizing exactly how much women contribute to the dialogue and story of these games, especially when compared to their male peers. For non-female gamers, this visualization can shed light on the disparities between male and female characters in Resident Evil, allowing them to think more critically about the games and their messaging.

In order to visualize women’s roles in the Resident Evil series across decades of software and hardware advancement, we chose to use the most objective and quantifiable data available: the characters’ dialogue. By utilizing the most direct and consistent metric, we would be able to quantify who spoke most and what they spoke about, which would give us a clearer idea of how these characters moved the story forward, if they did so at all.

To analyze this data, we first needed to quantify it. Our team found fan-made scripts of thirteen Resident Evil games: ten mainline games (Resident Evil 0, Resident Evil 1, Resident Evil 2, Resident Evil 3 - Nemesis, Resident Evil - Code: Veronica, Resident Evil 4, Resident Evil 5, Resident Evil 6, Resident Evil 7, and Resident Evil Village) and the three remakes (Resident Evil 2, Resident Evil 3, and Resident Evil 4). We acknowledged that these scripts were fan-made, and thus reflected the passion and subjectivity of each transcriptionist, but decided to move forward and implement strategies to normalize the data. We first attempted to use web scraping to obtain the scripts, but were continually blocked, despite not violating any of the websites’ terms. To circumvent this, we copied and pasted the contents of a GameFAQs or Game Scripts Wiki webpage into a text (.txt) file. Once we had these thirteen scripts, we tried various methods of cleaning the data: hand-weeding to isolate dialogue, Python and regex to remove large blocks of text and standardize formatting across styles, and cross-referencing game wikis and YouTube videos to clarify ambiguous characters. More information about this process can be found [here] and [here] in Jupyter notebooks created by Nichole, one of this project’s contributors.

What we found was interesting, if not surprising. Overall, 36% of Resident Evil’s characters were female, 57.6% were male, and 6.4% were N/A (non-identifiable or non-gendered). (This accounts for all characters, not just playable ones.) Female characters tended to speak less, with fewer instances of speech overall. Main characters tended to speak most, of course, but the top three speakers were Leon, with 16.3% of all dialogue, Chris with 9.1%, and Claire with 7.0%. Python graphs that explore this data, along, with many others, are viewable [here]. After quantitative analysis came qualitative questions: what were these characters actually talking about?

Our team incorporated two methods of topic modeling character dialogue. In the [topic_modeling] folder, the [re2_sklearn.ipynb] describes the two methods in detail, as well as the reasons we selected Resident Evil 2 and its remake for topic and character analysis. Moving forward to the [re2_remake_sklearn.ipynb], the remake is further analyzed and the two games are compared with the results by LDA python. For interactive visualization generated from the LDA python results, [re2_pyldavis_visualization.html] and [re2_remake_pyldavis_visualization.html] provide downloadable html graphs for the topics and words generated. The second method of topic analysis was utilizing MALLET to break down Resident Evil 2’s topics by character, then comparing this data to the same process applied to the game’s remake. The 2019 remake offers change for Claire, who has more dialogue in the remake, and is less tied to male characters. More information on this process, as well as heat maps and design decisions can be visualized [here]. In addition, MALLET was used to create lists of words to visualize as word clouds, which can be viewed [here]. Lastly, one of our contributors used Python to analyze the dialogue in Resident Evil 2 and Resident Evil 2’s remake to see who used the most action words, thus contributing the most to the action of the story, which can be visualized [here]. Female characters actually used more verbs, which was surprising, and worth further inquiry.

This project was limited in both time and scope; our group had further questions on if the differences in dialogue were as prevalent in main characters, playable or not, and how other games would compare to their remakes, among other questions. Shinji Mikami, the creator of the Resident Evil series, spoke about his stance on female characters in a 2014 Guardian article: “I write women characters who discover their independence as the game progresses, or who already know they are independent but have that tested against a series of challenges.” Knowing that there is a diverse player base of Resident Evil that has built up around the creator’s intent has encouraged us to pursue this project in order to better understand how the RE universe reflects its player base, as well as what it does not reflect. In a world that is ripe with games and flush with so many game developers, gamers choose and care about the games they play for a reason: this data visualization can not only help gamers see what they’re playing, it can show the ways games can improve.

---
## Bibliography

1. **Entertainment Software Association (ESA), 2024**  
   [Essential Facts About the U.S. Video Game Industry](https://www.theesa.com/resources/essential-facts-about-the-us-video-game-industry/2024-data/)  
   Accessed: 12 December 2024

2. **C, M. ‘Millers_C’ (2008)**  
   Resident Evil 2 (1998) - Game Script - PC - by millers_c - GameFAQs  
   [Link](https://gamefaqs.gamespot.com/pc/198456-resident-evil-2-1998/faqs/32821)  
   Accessed: 13 December 2024

3. **GAim4A (2022a)**  
   Resident Evil 6 Transcript  
   [Link](https://game-scripts-wiki.blogspot.com/2021/06/resident-evil-6-transcript.html)  
   Accessed: 12 December 2024

4. **GAim4A (2022b)**  
   Resident Evil 8 Village Full Transcript  
   [Link](https://game-scripts-wiki.blogspot.com/2021/05/resident-evil-8-village-full-transcript.html)  
   Accessed: 12 December 2024

5. **GAim4A (2022c)**  
   Resident Evil 2 (2019) Full Transcript  
   [Link](https://game-scripts-wiki.blogspot.com/2019/07/resident-evil-2-2019-full-transcript.html)  
   Accessed: 12 December 2024

6. **GAim4A (2022d)**  
   Resident Evil 3 (2020) Full Transcript  
   [Link](https://game-scripts-wiki.blogspot.com/2020/04/resident-evil-3-2020-full-transcript.html)  
   Accessed: 12 December 2024

7. **GAim4A (2022e)**  
   Resident Evil Revelations Transcript  
   [Link](https://game-scripts-wiki.blogspot.com/2018/09/resident-evil-revelations-transcript.html)  
   Accessed: 12 December 2024

8. **GAim4A (2024)**  
   Resident Evil 7 Full Transcript  
   [Link](https://game-scripts-wiki.blogspot.com/2018/12/resident-evil-7-full-transcript.html)  
   Accessed: 12 December 2024

9. **Gibson, C. ‘War_Mech’ (2002)**  
   Resident Evil 0: HD Remaster for PlayStation 4 - GameFAQs  
   [Link](https://gamefaqs.gamespot.com/ps4/164548-resident-evil-0-hd-remaster/faqs/20253)  
   Accessed: 13 December 2024

10. **Headcrook (2005)**  
    Resident Evil 4 - Game Script - PlayStation 2 - by Headcrook  
    [Link](https://gamefaqs.gamespot.com/ps2/925156-resident-evil-4/faqs/40715)  
    Accessed: 13 December 2024

11. **Lukman, J. (2024)**  
    Leveling the Playing Field for Women in Gaming Across Asia and MENA - Niko Partners  
    [Link](https://nikopartners.com/leveling-the-playing-field-for-women-in-gaming/)  
    Accessed: 12 December 2024

12. **Patrick ‘RE2LeonS’ (2006)**  
    Resident Evil Code: Veronica X - Game Script - PlayStation 2 - by Re2LeonS - GameFAQs  
    [Link](https://gamefaqs.gamespot.com/ps2/445328-resident-evil-code-veronica-x/faqs/41999)  
    Accessed: 13 December 2024

13. **Ratio of Male to Female Players - Resident Evil 6 - GameFAQs (2013)**  
    [Link](https://gamefaqs.gamespot.com/boards/605603-resident-evil-6/65100695?page=15)  
    Accessed: 13 December 2024

14. **Resident Evil (Series) (2023)**  
    Resident Evil (Series) - Game Scripts Wiki  
    [Link](https://game-scripts-wiki.blogspot.com/p/resident-evil-series.html)  
    Accessed: 12 December 2024

15. **Saiyuki12 (2010)**  
    Resident Evil 3: Nemesis - Game Script - PlayStation - by Saiyuki12 - GameFAQs  
    [Link](https://gamefaqs.gamespot.com/ps/198459-resident-evil-3-nemesis/faqs/60207)  
    Accessed: 13 December 2024

16. **Shinji Mikami: The Godfather of Horror Games (2014)**  
    The Guardian  
    [Link](https://www.theguardian.com/technology/2014/sep/30/shinji-mikami-evil-within-resident-evil)  
    Accessed: 12 December 2024

17. **Wiki, C. to R.E. (no date)**  
    Resident Evil 6 Cutscenes - Resident Evil Wiki  
    [Link](https://residentevil.fandom.com/wiki/Category:Resident_Evil_6_cutscenes)  
    Accessed: 12 December 2024


