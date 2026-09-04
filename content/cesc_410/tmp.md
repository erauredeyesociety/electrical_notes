ok, now working in the /home/devel/electrical_notes/content/cesc_410

i am now trying to setup /home/devel/electrical_notes/content/cesc_410/labs_and_projects

we have the same professor as from the cec320 course, so we should be able to use alot of the findings and lessons learned from /home/devel/electrical_notes/content/cec_320/labs_and_projects/ and basically be able to copy alot of them, but rather than stm32 cubeide we are working more with python i think? perhaps we will ahve to see how the next labs go, but we have lab0 right now that we need to put in its own folder and the get lab 0 done, so get the labs and projects folder all setup, get the documentation for it all setup so that they are good guides for reading the lab files and assessing what is going on and seeing if any downloaded files are missiong, etc... make snese? and then we will be using python, so we can just ad a git ignore into the labs and projects folder for all pycache things and venv things make sense? we might setup virtual environments in the class, and if they are named something other than venv, then we jsut have to put notes to gitignore them, and tehn we could just have readmes for the labs that get made and other stuff make snes? that way we keep track of all commands to run and what all to do to reproduce the lab and distill it from lab documents and what acutally happened. make snese? please ask questions if you need, it does not need to be setup as a chilld project, but please adhere  to ~/llm-project-bootstrap standards for aggressive minimalism and modularity for the documentation make snese? and that does nto mean you need to make 20 files for every project make sense?



also does the lab documents specify image should be output in svg or in png? i would much rather prefer png or something, or how about we output in both svg and png. make sense? and also we need to keep separate the code we use for the lab, and then the code we use to automate all the lab procedures, this needs to be specified in the reference documents for the md files that you will wnat to be referncing i nthe fugure, make sense? and then also they will be able to tell you how to strucutre lab reports if needed, just like from the cec 320 course or something, make snese? but yes we need to make the code for the labs completely standalone, but then make automation code that gets everything done that we need separae but able to use the lab code to get the lab done. make snese? we don't want to come off as having automated the entire lab if we turn in lab code, i just wanted to make sure this was documented approprirately and stuff. make snese? please ask questions as you need. otherwise continue.


then also for lab code and the automation code, we want to add comments for what each step of the code does, again we ned to put documetns for referecne in the reference docs folder so that we can have the agressive minimal modualrity and have the files that need to be standalone be standalone, but then be able to have brief explanations for what happens in the code, like "perform the fourier transform for x" make sense? that way we can use al lthis code and lab work and documentation to really help out later. unsure if i also want to have outputs not only in markdown but also in latex for lab output documetns jsut so that we can really be able to clarify math equations used, and you don't need to render the latex to pdf, but make sure it renders without issue, then delete the pdfs afterwards, that can be a common render lab reports bash script or something, let me know if you need latex tools installed, because also i want to be able to copy and paste the latex files into overleaf and render them there, make snese? then i am also unsure if we really need all the images we render in git or we can just gitignore them, because lab automation code should be able to be run and generate the images just fine. make snes? images really take up space in git and i don't want to blaot things unnecesarily. and thank you for bringing up 

py-pkg-1c-uv-qg.md

i will look around for it somewhere, otherwise this should be enough for you to continue as needed.


ok well we need a way to automate getting code into submissions, like we don't want to have all of our comments in our code, it seems to ai upon submission make sense? we just want the code that simply works. so like use regex to remove comments, and then in the submisison maker script just prepend or append whatever comments are needed for the lab number and whatever the lab pdf says. but that is if we need to submit code, so in the reference docs make sure to state that we need to work to clarify what submissions will actually entail. make sense? so like this lab00 only need the figures right? otherwise uv and everyting else is already setup and working and we have everyting to get done for all labs this semester?


ok perhaps we don't always need to be making file comments in all of our files, it might get messy upon submission - or did you get that comments remover tool workgin? so that we only comment exactly where lab files tell us? make sense? this is a point of confusion for me right now otherwise continue.


"""
Confirmed — baseURL: https://erauredeyesociety.github.io/electrical_notes/. This repo publishes content/ to a public GitHub Pages site.
"""

don't worry about this or publishing content at all, and the git repo aspect is not applicable for this project make sense? and docuemtn this in the refernce docs for later just in case there is any confusion


great we are done with the live demo, can you make the zip folder with the figures. perhpas we should put the figures in a super simple minimal markdwon / latex file so that we can have a documetn with all the pictures and just submit that, make sense? how about we have that report that only has images in it and teh images zipped then i will submit that. make snes? and submissino requirements might change in the future so document that but otherwise yes lets just get this done right now
Show less


all zip files should be git ignored. then also yes render reports i guess we need to only have on script actually rende the pdf make sense? perhaps we don't want to delete the report pdf because we can just gitignore all report.pdf files in all lab* folders make sense? please document all these things and get everything updated as needed. lets get this done.

ok last thing, pelase dont let things like """
% Render:  tools/render_reports.sh lab00 --keep
% Package: tools/make_submission.sh lab00 nelson-gatlin --figures
"""

or mentions to any scripts outside of code for the actual lab itself get into the actual report documents and get zipped, make sense? so you need to redo the reports or something, and/or update the report template or somthing. make sense?




ok now we have /home/devel/electrical_notes/content/cesc_410/hw

and i want to treat it just like 
/home/devel/electrical_notes/content/cesc_410/labs_and_projects

make snese? again please make a findings and prompt document for the hw stuff but of course it might be slightly differnt every time, so just like how 

/home/devel/electrical_notes/content/stat_412
and
/home/devel/electrical_notes/content/cec_320
and
/home/devel/electrical_notes/content/cec_315

worked in hte past we really need detailed step by step explanations for every problem and then the solutions document is really the short and sweet condensed version for just the answers, but we need to have all the work for each probelm on every assignemnt in tis own tex file make sense? and i dont' want to mess around with markdown for the homework, just use straight latex. also make sure you can cross reference and make use of the 

/home/devel/electrical_notes/content/cesc_410/lectures
and 
/home/devel/electrical_notes/content/cesc_410/labs_and_projects

content in those folders, perhaps make a python script to get all their text or something well also we were trying to setup 

/home/devel/electrical_notes/ocr_handler

to solve the grabbing the text problem as well, i am just trying to be able ot set you up for success when solving probelms so that you don't have to do so much internet searching all the time and you can just use the course materials, and the course materials might not always be enough. make sense? pehrpas we should start a docs-rag for htis repo? like look into ~/exudeai/rag-bootstrap ? this si because there are so many docuemtns in this repo that might help you among all the courses you could make different knowledge bases but then with docs rag be able to look thorugh them individually or overall make snese? and then likee ~/skytracker_v2/docs-rag they use a remote ollama instance port forwareded to locally perhaps you ned to copy the scripts so that you can run them as you need to make sure the tunnels are up and not stale thigns like that and you could just put the scripts into ./docs-rag/port_forwards/ when you need so its all good. is this all makeing sense what i watn? also howework submissions will depende per assignment but usually we will not be writing code or zipping files like in the labs. make sense? let me know if you have questions.

ok so parallel work for you to do, we now have new stuff in the /home/devel/electrical_notes/content/cpsc_462/class_materials/ folder and i want to be able to pull hte text out of the pdfs and stuff so that i can understand what all is going on perahps make a 

/home/devel/electrical_notes/content/cpsc_462/md_notes or something folder because we are going to be working on wireshark stuff right now, so again just stuff in parallel.






ok and then also work in paralell to spawn more workflows for is that /home/devel/electrical_notes/content/cesc_470 i need you to be starting to get md_transcripts of hte pdfs and make like a /home/devel/electrical_notes/content/cesc_470/pdf_transcripts/ and then also /home/devel/electrical_notes/content/cesc_470/md_notes/ where you basically make better tutorials with citations for brief theory explanations and also worked examples because we are going to be having quizes soon make sense? so pelase get this done as well. i guess also if you watn to make the ocr handler attempt to get the text layer from a pdf before doing ocr, then have ocr done and have the two side by side as outputs fro the user  to beable to use or something? i just don't want all classes to have their own text extractors for pdfs i want it all centralized, pehraps ocr handler could have an argument to to "just get text layer" and sometimes there will be no text layer and then sometimes "do ocr" and sometimes there will be no reason to do ocr or ocr after processing and review will not return anything different than what was in the text layer mkae snese? hope htis is clearn, and also you seem to be having lots of issues wit hthe docs rag, you can ssh to the 

ssh devel@10.231.80.91

because there should be an active claude session on the remote computer located at their ~/exudeai/ so you might be able to send a message over the claude bus to them or something? you would just have to setup a message bus monitor to remotely monitor or something? that way you can communicate with them if they have updates or patches remotely for the docs rag, but then there is also the fact taht the local ~/exudeai/ and the remote ~/exxudeai are clones of the same git repo so we might need to coordinate how updates are recieved, unsure make sense? so it is confusing but we shuold be able to figure out remote repos coordination. becuase ~/skytracker_v2 has the same issue where there is a local copy and then a remote ~/skytracker_v2 on the same remote server make sense? so please ask questions as neede and don't act to hastily.




ship tutorials from text layer right now, and spawn parallel workflwos to work on the ocr handler, rememebr ocr handler is an entire child project in of itself so it needs to be treated with llm project bootstrap doctrine as well, we don't want o just half ass something and have it turn out bad, perhaps more research and docs and planning needs to be done on it as well because the example repos it might be picking apart might not be the best solutions either. make sense? otherwies continue and let me know if any other questions.



ok great, now i want to get /home/devel/electrical_notes/content/cesc_470/hw/HW1.pdf completely done make sure to include fully worked step by step solution partial latex files and then have the completed solutions latex file make snese? so for homework, quizes, and exams for all courses i want worke step by step solutions for each problem with citations and then use those partials to make the quick condensed answers docuemtn, pelase update ./docs in the docs folder perhaps also apply a ~/llm-project-bootstrap/PROMPTS.md "catch up" pormpts for this repo so that the docs folder is modernized, and you don't have to worry about going back into older courses and redoing the HW and quized and tests. please only apply this new doctrine to the cesc_470, the cesc_410, the cpsc_462 courses those are the newset courses and then courses in the future will also need this doctrine applied to them, make sense? please ask questions as needed and spawn multiple workflows to get everything done.