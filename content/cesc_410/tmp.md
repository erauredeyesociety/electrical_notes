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