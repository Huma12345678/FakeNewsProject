#!/usr/bin/env python
# coding: utf-8

# In[5]:


import import_ipynb


# In[6]:


import pandas as pd
import BAGofWORDS as b
import numpy as np


# In[7]:


from sklearn.svm import SVC
classifier = SVC(kernel='linear')

 # Fit classifier according to X, y
classifier.fit(b.count_train, b.y_train) 


# In[8]:


# Perform classification on an array of test vectors X.
y_pred = classifier.predict(b.count_test)


# In[9]:


from sklearn.metrics import classification_report, confusion_matrix, accuracy_score


# In[10]:


a=confusion_matrix(b.y_test,y_pred)
a1=a.flatten()
print(a1)
#[TP, FN, FP, TN]


# In[11]:


print(classification_report(b.y_test,y_pred))


# In[12]:


print(accuracy_score(b.y_test,y_pred))


# In[13]:


import matplotlib.pyplot as plt


# In[14]:


labels = 'TruePositive', 'FalseNegative', 'FalsePositive', 'TrueNegative'
colors = ['gold', 'yellowgreen', 'lightcoral', 'lightskyblue']

# Plot
plt.pie(a1, labels=labels, colors=colors,
autopct='%1.1f%%', shadow=True, startangle=140)

plt.axis('equal')
plt.show()


# In[15]:


import pickle
#save our model as a pickle object in Python
with open('svm', 'wb') as picklefile:
    pickle.dump(classifier,picklefile)


# In[16]:


# tests=["A week before Michael T. Flynn resigned as national security adviser, a sealed proposal was   to his office, outlining a way for President Trump to lift sanctions against Russia. Mr. Flynn is gone, having been caught lying about his own discussion of sanctions with the Russian ambassador. But the proposal, a peace plan for Ukraine and Russia, remains, along with those pushing it: Michael D. Cohen, the president’s personal lawyer, who delivered the document Felix H. Sater, a business associate who helped Mr. Trump scout deals in Russia and a Ukrainian lawmaker trying to rise in a political opposition movement shaped in part by Mr. Trump’s former campaign manager Paul Manafort. At a time when Mr. Trump’s ties to Russia, and the people connected to him, are under heightened scrutiny  —   with investigations by American intelligence agencies, the F. B. I. and Congress  —   some of his associates remain willing and eager to wade into   efforts behind the scenes. Mr. Trump has confounded Democrats and Republicans alike with his repeated praise for the Russian president, Vladimir V. Putin, and his desire to forge an   alliance. While there is nothing illegal about such unofficial efforts, a proposal that seems to tip toward Russian interests may set off alarms. The amateur diplomats say their goal is simply to help settle a grueling,   conflict that has cost 10, 000 lives. “Who doesn’t want to help bring about peace?” Mr. Cohen asked. But the proposal contains more than just a peace plan. Andrii V. Artemenko, the Ukrainian lawmaker, who sees himself as a   leader of a future Ukraine, claims to have evidence  —   “names of companies, wire transfers”  —   showing corruption by the Ukrainian president, Petro O. Poroshenko, that could help oust him. And Mr. Artemenko said he had received encouragement for his plans from top aides to Mr. Putin. “A lot of people will call me a Russian agent, a U. S. agent, a C. I. A. agent,” Mr. Artemenko said. “But how can you find a good solution between our countries if we do not talk?” Mr. Cohen and Mr. Sater said they had not spoken to Mr. Trump about the proposal, and have no experience in foreign policy. Mr. Cohen is one of several Trump associates under scrutiny in an F. B. I. counterintelligence examination of links with Russia, according to law enforcement officials he has denied any illicit connections. The two others involved in the effort have somewhat questionable pasts: Mr. Sater, 50, a   pleaded guilty to a role in a stock manipulation scheme decades ago that involved the Mafia. Mr. Artemenko spent two and a half years in jail in Kiev in the early 2000s on embezzlement charges, later dropped, which he said had been politically motivated. While it is unclear if the White House will take the proposal seriously, the diplomatic freelancing has infuriated Ukrainian officials. Ukraine’s ambassador to the United States, Valeriy Chaly, said Mr. Artemenko “is not entitled to present any alternative peace plans on behalf of Ukraine to any foreign government, including the U. S. administration. ” At a security conference in Munich on Friday, Mr. Poroshenko warned the West against “appeasement” of Russia, and some American experts say offering Russia any alternative to a    international agreement on Ukraine would be a mistake. The Trump administration has sent mixed signals about the conflict in Ukraine. But given Mr. Trump’s praise for Mr. Putin, John Herbst, a former American ambassador to Ukraine, said he feared the new president might be too eager to mend relations with Russia at Ukraine’s expense  —   potentially with a plan like Mr. Artemenko’s. It was late January when the three men associated with the proposed plan converged on the Loews Regency, a luxury hotel on Park Avenue in Manhattan where business deals are made in a lobby furnished with leather couches, over martinis at the restaurant bar and in private conference rooms on upper floors. Mr. Cohen, 50, lives two blocks up the street, in Trump Park Avenue. A lawyer who joined the Trump Organization in 2007 as special counsel, he has worked on many deals, including a   tower in the republic of Georgia and a   mixed martial arts venture starring a Russian fighter. He is considered a loyal lieutenant whom Mr. Trump trusts to fix difficult problems. The F. B. I. is reviewing an unverified dossier, compiled by a former British intelligence agent and funded by Mr. Trump’s political opponents, that claims Mr. Cohen met with a Russian representative in Prague during the presidential campaign to discuss Russia’s hacking of Democratic targets. But the Russian official named in the report told The New York Times that he had never met Mr. Cohen. Mr. Cohen insists that he has never visited Prague and that the dossier’s assertions are fabrications. (Mr. Manafort is also under investigation by the F. B. I. for his connections to Russia and Ukraine.) Mr. Cohen has a personal connection to Ukraine: He is married to a Ukrainian woman and once worked with relatives there to establish an ethanol business. Mr. Artemenko, tall and burly, arrived at the Manhattan hotel between visits to Washington. (His wife, he said, met the first lady, Melania Trump, years ago during their modeling careers, but he did not try to meet Mr. Trump.) He had attended the inauguration and visited Congress, posting on Facebook his admiration for Mr. Trump and talking up his peace plan in meetings with American lawmakers. He entered Parliament in 2014, the year that the former Ukrainian president Viktor Yanukovych fled to Moscow amid protests over his economic alignment with Russia and corruption. Mr. Manafort, who had been instrumental in getting Mr. Yanukovych elected, helped shape a political bloc that sprang up to oppose the new president, Mr. Poroshenko, a wealthy businessman who has taken a far tougher stance toward Russia and accused Mr. Putin of wanting to absorb Ukraine into a new Russian Empire. Mr. Artemenko, 48, emerged from the opposition that Mr. Manafort nurtured. (The two men have never met, Mr. Artemenko said.) Before entering politics, Mr. Artemenko had business ventures in the Middle East and real estate deals in the Miami area, and had worked as an agent representing top Ukrainian athletes. Some colleagues in Parliament describe him as corrupt, untrustworthy or simply insignificant, but he appears to have amassed considerable wealth. He has fashioned himself in the image of Mr. Trump, presenting himself as Ukraine’s answer to a rising class of nationalist leaders in the West. He even traveled to Cleveland last summer for the Republican National Convention, seizing on the chance to meet with members of Mr. Trump’s campaign. “It’s time for new leaders, new approaches to the governance of the country, new principles and new negotiators in international politics,” he wrote on Facebook on Jan. 27. “Our time has come!” Mr. Artemenko said he saw in Mr. Trump an opportunity to advocate a plan for peace in Ukraine  —   and help advance his own political career. Essentially, his plan would require the withdrawal of all Russian forces from eastern Ukraine. Ukrainian voters would decide in a referendum whether Crimea, the Ukrainian territory seized by Russia in 2014, would be leased to Russia for a term of 50 or 100 years. The Ukrainian ambassador, Mr. Chaly, rejected a lease of that kind. “It is a gross violation of the Constitution,” he said in written answers to questions from The Times. “Such ideas can be pitched or pushed through only by those openly or covertly representing Russian interests. ” The reaction suggested why Mr. Artemenko’s project also includes the dissemination of “kompromat,” or compromising material, purportedly showing that Mr. Poroshenko and his closest associates are corrupt. Only a new government, presumably one less hostile to Russia, might take up his plan. Mr. Sater, a longtime business associate of Mr. Trump’s with connections in Russia, was willing to help Mr. Artemenko’s proposal reach the White House. Mr. Trump has sought to distance himself from Mr. Sater in recent years. If Mr. Sater “were sitting in the room right now,” Mr. Trump said in a 2013 deposition, “I really wouldn’t know what he looked like. ” But Mr. Sater worked on real estate development deals with the Trump Organization on and off for at least a decade, even after his role in the stock manipulation scheme came to light. Mr. Sater, who was born in the Soviet Union and grew up in New York, served as an executive at a firm called Bayrock Group, two floors below the Trump Organization in Trump Tower, and was later a senior adviser to Mr. Trump. He said he had been working on a plan for a Trump Tower in Moscow with a Russian real estate developer as recently as the fall of 2015, one that he said had come to a halt because of Mr. Trump’s presidential campaign. (Mr. Cohen said the Trump Organization had received a letter of intent for a project in Moscow from a Russian real estate developer at that time but determined that the project was not feasible.) Mr. Artemenko said a mutual friend had put him in touch with Mr. Sater. Helping to advance the proposal, Mr. Sater said, made sense. “I want to stop a war, number one,” he said. “Number two, I absolutely believe that the U. S. and Russia need to be allies, not enemies. If I could achieve both in one stroke, it would be a home run. ” After speaking with Mr. Sater and Mr. Artemenko in person, Mr. Cohen said he would deliver the plan to the White House. Mr. Cohen said he did not know who in the Russian government had offered encouragement on it, as Mr. Artemenko claims, but he understood there was a promise of proof of corruption by the Ukrainian president. “Fraud is never good, right?” Mr. Cohen said. He said Mr. Sater had given him the written proposal in a sealed envelope. When Mr. Cohen met with Mr. Trump in the Oval Office in early February, he said, he left the proposal in Mr. Flynn’s office. Mr. Cohen said he was waiting for a response when Mr. Flynn was forced from his post. Now Mr. Cohen, Mr. Sater and Mr. Artemenko are hoping a new national security adviser will take up their cause. On Friday the president wrote on Twitter that he had four new candidates for the job."]

# # encode document
# vector = b.count_vectorizer.transform(tests)

# # summarize encoded vector
# print(vector.shape)
# print(vector.toarray())

# pred=classifier.predict(vector.toarray())
# print(pred)

