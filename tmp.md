ok so something to note, that /home/devel/electrical_notes/content/cesc_410/lectures has pdfs in it but also there is a decent amount of handwriting and then also there are the "*plw*" pdf files wehre the instructor adds custom notes while lecturing on the otehr pdf materials. make snese? and this was the case in cec 320 and potentially other courses, so we need to figure out a good solution for OCR pdfs for text extraction, and i am unsure if it is more effective to just have the output be in latex or in markdown format, it is very importatn to be able to get the equations and the graphs from the pdfs and try to hold as images to insert into markdown files for repors or latex repors make sense? i have no idea how to describe this bettter other than it is needed very much and actaully this should be its own project, not in electrical notes, electrical notes is too big, well actually if we follow llm project bootstrap doctrine well then we can make a child proejct and make it super effective, perhaps we need to work on cleaning up the git history of electrical notes so that it is not so large? i think that would help as well. don't setup the child proejct just yet, just make a ./tmp_ocr_child.md document in the root of this repo so that we understand what all the new project will entail and scope and stuff so we can talk about it later. make sense?





ok well thank you for the findings, so perhaps the software that the professor uses has automatic text recognition? well lets test, can you read to me what the handwritten notes are on page 5 of /home/devel/electrical_notes/content/cesc_410/lectures/f26_lctr02_DT signals and systems-plw.pdf? i will give you grace that you might not be able to differentiate between the normal black ink of the lecture and the red ink of the handwritten notes. but you need to be bale to tell me everything that is going on and describe what is happening after getting me a verbatim transcript of everything. and the verbatim transcript needs to render equestions properly, which is why i am torn betwwen markdown vs latex output for that. make sense? pelase make a ./tmp/ fodler in the root of this repo as sort of scratch that can be gitignored and in the future deleted. make snese?


ok well whatever you are doing, i wnat to be able to automate it in python because i don't want you burning tokens make sense? perhpas just make a new folder called ./ocr_handler and then use the ~/llm-project-bootstrap "initialize" prompt to get it off the groud, and then research and document existing ocr methods and how effective claude ocr is or what they use and what chatgpt ocr uses i need something that can run locally and perhpas use my local gpu, apparently "besu" ocr is available on github and can be used or something? so perhaps there are really highly rated git repos that you could clone into ~/tmp/ and then pick them apart for reseach and figure out how they work and their documentation and hten record documetnation yourself, of course following llm project bootstrap doctrine, i want o get this fully done and tehse scripts should not really be that large i really question a script hta is over 300 lines make sense? we don't need complicated command interface, just file, page, tehn scanning procedures, then option for latex or mardkwon math output, make sense? then separately we would do regex scanning or whatever for pdf files in generarl and we can work out how to handle input files nad where the output files will be but you can make a tmp folder in this new child project to be the out put directory for now make sense? and also we want to basically take graphs and screenshot and crop them into images we want to have minimal images and then evenually get the the point where we have a full new pdf with all equations in text format and images and we can delete the images from disk make sense? 



sorry, i meant baidu ocr,

https://github.com/baidu/Unlimited-OCR

https://huggingface.co/baidu/Unlimited-OCR

that is the inspiration for this prooject make sense? so please perhaps git clone that and see if you can pick it apart and document fingind sfor the ocr handler project  make ssense? spawn multiple more agetns as needed and also try to leverage local gpu as you can. 





ok so you are fully done and have applied a ~/llm-project-bootstrap "save progress" prompt to the ocr handler project? if not pelase do so, and tehn also please make sure to gitignore large files you donwload in the ocr handler project things like that and also be smart about git ignoring pycache and more. make sense? get this all done so i can just git commit to save progress thanks