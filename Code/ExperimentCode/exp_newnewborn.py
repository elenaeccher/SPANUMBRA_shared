# -*- coding: utf-8 -*-
"""
Created on Tue Sep 21 18:51:07 2021

@author: Mathilde JOSSERAND
"""

from __future__ import print_function
from psychopy import visual, core, event, info, gui, data
from PIL import Image
import cv2 as cv
import pandas as pd
import random
import shutil
import os


# ### 
# expInfo = {'participant':'1'}
# expInfo['dateStr'] = data.getDateStr()
# dictDlg = gui.DlgFromDict(dictionary=expInfo,
#         title='TestExperiment', fixed=['ExpVersion'])
# if dictDlg.OK:
#     print(expInfo)
# else:
#     print('User Cancelled')
#     core.quit()  # the user hit cancel so exit
 
def newnewborn(condition, part_id, path):
    
    pathfiles = path + 'Newnewborn/'

    # Create file with results
    fileName = "Participant" + str(part_id) + '_Date' +  data.getDateStr()
    dataFile = open(pathfiles + 'results/'+ fileName+'.csv', 'w')  
    dataFile.write('amorce, test, time, resp, position, condition, type_test, key_pressed, feedback \n')
    
    
    mywin = visual.Window(size=(1800, 900), allowGUI=False, monitor='testMonitor', units='deg',colorSpace='rgb',color="black", fullscr=False)
    mywin.setMouseVisible(False)
    
    # load flashing cross
    texte_cross = visual.TextStim(win=mywin, units='pix', text="+", font='', pos=(0,0), color="white", height=100, opacity=1)
    
    # disposition of the stimuli and size 
    space_between_stim = 17 # in visual angle (deg)
    size_stim = 17 # in visual angle (deg)

    time_feedback = 1.1
    time_after_feedback = 1.5
    
    
    # load stimuli
    exp1_4 = visual.ImageStim(win=mywin, pos=[0,0], size=[size_stim,size_stim], image=pathfiles+"stimuli/exp1_4.jpg", units="deg")
    exp1_12 = visual.ImageStim(win=mywin, pos=[0,0], size=[size_stim,size_stim], image=pathfiles+"stimuli/exp1_12.jpg", units="deg")
    exp1_36 = visual.ImageStim(win=mywin, pos=[0,0], size=[size_stim,size_stim], image=pathfiles+"stimuli/exp1_36.jpg", units="deg")
    exp2_4 = visual.ImageStim(win=mywin, pos=[0,0], size=[size_stim,size_stim], image=pathfiles+"stimuli/exp2_4.jpg", units="deg")
    exp2_4_12 = visual.ImageStim(win=mywin, pos=[0,0], size=[size_stim,size_stim], image=pathfiles+"stimuli/exp2_4_12.jpg", units="deg")
    exp2_36 = visual.ImageStim(win=mywin, pos=[0,0], size=[size_stim,size_stim], image=pathfiles+"stimuli/exp2_36.jpg", units="deg")
    exp2_36_12 = visual.ImageStim(win=mywin, pos=[0,0], size=[size_stim,size_stim], image=pathfiles+"stimuli/exp2_36_12.jpg", units="deg")
    white_box = visual.ImageStim(win=mywin, pos=[0,0], size=[size_stim,size_stim], image=pathfiles+"stimuli/exp_white.jpg", units="deg")
    
    increase_message = visual.TextStim(mywin, pos=[0,+3],text="Press a button ONLY if the number INCREASES", color="white")
    decrease_message = visual.TextStim(mywin, pos=[0,+3],text="Press a button ONLY if the number DECREASES", color="white")
    
    ask_message = visual.TextStim(mywin, pos=[0,+3],text="Has the participant understood the task? Press 'y' for 'yes', 'n' for no, and 'a' for 'abort'", color="white")

    # create happy and sad smiley (only for training)
    happy = visual.ImageStim(win=mywin, image=pathfiles+"happy2.png", units="pix", size=(200, 200))
    sad = visual.ImageStim(win=mywin, image=pathfiles+"sad2.png", units="pix", size=(200, 200))
    
    

    def run_exp(type_stim1, type_stim2, position_stim, condition2, type_test):  
          
        mywin.flip()
        core.wait(time_after_feedback)    
        
        texte_cross.draw()
        mywin.flip()
        if type_test == "testing" or type_test == "training":
            core.wait(0.5)
        elif type_test == "training_slow":
            allKeys=event.waitKeys()

        mywin.flip()
        core.wait(0.2)    

        if type_stim1 == 4 :
            exp1_4.setPos([0,0])
            exp1_4.draw()
        elif type_stim1 == 12:
            exp1_12.setPos([0,0])
            exp1_12.draw()
        elif type_stim1 == 36:
            exp1_36.setPos([0,0])
            exp1_36.draw()
        mywin.flip()
        
        if type_test == "testing" or type_test == "training":
            core.wait(0.5)
        elif type_test == "training_slow":
            allKeys=event.waitKeys()

        
        mywin.flip()
        core.wait(0.2)
        
        if type_stim2 == 4:
            exp1_4.setPos([position_stim,0])
            exp1_4.draw()
        elif type_stim2 == 12:
            exp1_12.setPos([position_stim,0])
            exp1_12.draw()
        elif type_stim2 == 36:
            exp1_36.setPos([position_stim,0])
            exp1_36.draw()
    
        mywin.flip()
        
        timer = core.Clock()
        thisResp=None
        allKeys=[]
        RT = core.Clock()
        
        while thisResp==None :
            #allKeys=event.waitKeys()
            if type_test=="training" or type_test == "training_slow":
                allKeys=event.waitKeys(4, 'space, 2, escape, q', timeStamped=timer)
            elif type_test == "testing":
                allKeys=event.waitKeys(3, 'space, 2, escape, q', timeStamped=timer)
                
            if allKeys:
        
                for thisKey in allKeys:
                    mykey = thisKey[0]
                    mywin.flip()
                    rt = RT.getTime()
                    core.wait(0.1)
                    if thisKey[0]=='space' or thisKey[0]=='2' :
                        if type_stim1 < type_stim2 and condition2 == "increase":
                            thisResp=1
                            happy.draw()
                            mywin.flip()
                            core.wait(time_feedback)
                        elif type_stim1 > type_stim2 and condition2 == "increase" :
                            thisResp=0
                            sad.draw()
                            mywin.flip()
                            core.wait(time_feedback)
                        elif type_stim1 < type_stim2 and condition2 == "decrease":
                            thisResp=0
                            sad.draw()
                            mywin.flip()
                            core.wait(time_feedback)
                        elif type_stim1 > type_stim2 and condition2 == "decrease" :
                            thisResp=1
                            happy.draw()
                            mywin.flip()
                            core.wait(time_feedback)
                       
                    elif thisKey[0]=="q":
                        mywin.close()
                        core.quit() 
                    elif thisKey[0]=="escape":
                        mywin.close()
                        core.quit() 
                    break
                
                event.clearEvents()  
            else:
                mykey = "nothing"
                if type_stim1 > type_stim2 and condition2 == "increase":
                    thisResp=1
                    happy.draw()
                    mywin.flip()
                    core.wait(time_feedback)
                elif type_stim1 < type_stim2 and condition2 == "increase" :
                    thisResp=0
                    sad.draw()
                    mywin.flip()
                    core.wait(time_feedback)
                elif type_stim1 < type_stim2 and condition2 == "decrease":
                    thisResp=1
                    happy.draw()
                    mywin.flip()
                    core.wait(time_feedback)
                elif type_stim1 > type_stim2 and condition2 == "decrease" :
                    thisResp=0
                    sad.draw()
                    mywin.flip()
                    core.wait(time_feedback)
                    
                mywin.flip()
                core.wait(0.3)
                rt=RT.getTime()
                event.clearEvents() 
                
                break
        print(thisResp)
        dataFile.write('%i,%i,%f,%i,%i,%s,%s,%s,%s\n' %(type_stim1, type_stim2, rt, thisResp, position_stim, condition, type_test, mykey, "yes"))


    mycond= condition
    
    def training():
        
        if mycond == "increasing":

        # training : one of each

            increase_message.draw()
            mywin.flip()
            event.waitKeys()
        
            run_exp(36, 4, -15, "increase", "training_slow")
            run_exp(4, 12, -15, "increase", "training_slow")
            run_exp(12, 36, 15, "increase", "training_slow")
            run_exp(36, 4, 15, "increase", "training_slow")
            run_exp(12, 4, -15, "increase", "training_slow")
            run_exp(4, 36, -15, "increase", "training_slow")
            run_exp(36, 12, 15, "increase", "training")
            run_exp(4, 12, 15, "increase", "training")
            run_exp(12, 36, -15, "increase", "training")
            run_exp(12, 4, 15, "increase", "training")
            run_exp(4, 36, 15, "increase", "training")
            run_exp(36, 12, -15, "increase", "training")    
    
            # # additional pieces for training
            # run_exp(4, 12, -15, "increase", "training")
            # run_exp(36, 12, 15, "increase", "training")
            # run_exp(4, 36, 15, "increase", "training")
            # run_exp(36, 4, -15, "increase", "training")
            # run_exp(12, 4, 15, "increase", "training")
            # run_exp(4, 36, -15, "increase", "training")
            
        if mycond == "decreasing":
            
            decrease_message.draw()
            mywin.flip()
            event.waitKeys()
        
            run_exp(12, 4, 15, "decrease", "training_slow")
            run_exp(4, 12, 15, "decrease", "training_slow")
            run_exp(4, 36, 15, "decrease", "training_slow")
            run_exp(36, 4, -15, "decrease", "training_slow")
            run_exp(36, 12, 15, "decrease", "training_slow")
            run_exp(12, 4, -15, "decrease", "training_slow")
            run_exp(12, 36, 15, "decrease", "training")
            run_exp(4, 36, -15, "decrease", "training")
            run_exp(12, 36, -15, "decrease", "training")
            run_exp(36, 4, 15, "decrease", "training")
            run_exp(36, 12, -15, "decrease", "training")
            run_exp(4, 12, -15, "decrease", "training")
            
            # # additional pieces for training
            # run_exp(36, 12, 15, "decrease", "training")
            # run_exp(12, 4, 15, "decrease", "training")
            # run_exp(4, 36, -15, "decrease", "training")
            # run_exp(4, 36, 15, "decrease", "training")
            # run_exp(4, 12, -15, "decrease", "training")
            # run_exp(36, 4, -15, "decrease", "training")

    def testing():
        
        if mycond == "increasing":
            # testing for increase
            run_exp(12, 36, 15, "increase", "testing")
            run_exp(12, 4, -15, "increase", "testing")
            run_exp(4, 36, -15, "increase", "testing")
            run_exp(36, 4, 15, "increase", "testing")
            run_exp(12, 36, 15, "increase", "testing")
            run_exp(4, 36, -15, "increase", "testing")
            run_exp(12, 4, -15, "increase", "testing")
            run_exp(12, 36, -15, "increase", "testing")
            run_exp(4, 36, 15, "increase", "testing")
            run_exp(36, 4, -15, "increase", "testing")
            run_exp(4, 12, -15, "increase", "testing")
            run_exp(4, 36, -15, "increase", "testing")
            run_exp(36, 4, 15, "increase", "testing")
            run_exp(4, 12, 15, "increase", "testing")
            run_exp(12, 36, -15, "increase", "testing")
            run_exp(12, 4, 15, "increase", "testing")
            run_exp(4, 36, 15, "increase", "testing")
            run_exp(4, 12, -15, "increase", "testing")
            run_exp(12, 36, 15, "increase", "testing")
            run_exp(12, 36, 15, "increase", "testing")
            run_exp(4, 36, -15, "increase", "testing")
            run_exp(36, 4, -15, "increase", "testing")
            run_exp(4, 12, -15, "increase", "testing")
            run_exp(12, 36, 15, "increase", "testing")
            run_exp(4, 12, 15, "increase", "testing")
            run_exp(12, 36, -15, "increase", "testing")
            run_exp(12, 4, 15, "increase", "testing")
            run_exp(4, 36, 15, "increase", "testing")
            run_exp(4, 12, -15, "increase", "testing")
            run_exp(36, 12, 15, "increase", "testing")
            run_exp(4, 12, -15, "increase", "testing")
            run_exp(4, 12, 15, "increase", "testing")
            run_exp(36, 12, -15, "increase", "testing")
            run_exp(12, 36, -15, "increase", "testing")
            run_exp(4, 36, 15, "increase", "testing")
            run_exp(36, 12, 15, "increase", "testing")
            run_exp(36, 12, -15, "increase", "testing")
            run_exp(36, 4, -15, "increase", "testing")
            run_exp(12, 4, -15, "increase", "testing")
            run_exp(4, 36, -15, "increase", "testing")
            run_exp(36, 4, 15, "increase", "testing")
            run_exp(4, 12, 15, "increase", "testing")
            run_exp(12, 36, -15, "increase", "testing")
            run_exp(12, 4, 15, "increase", "testing")
            run_exp(4, 36, 15, "increase", "testing")
            run_exp(36, 12, 15, "increase", "testing")
            run_exp(36, 12, -15, "increase", "testing")
            run_exp(4, 12, 15, "increase", "testing")
            
        if mycond == "decreasing":
            # decrease exp
            run_exp(12, 4, 15, "decrease", "testing")
            run_exp(12, 36, 15, "decrease", "testing")
            run_exp(4, 12, -15, "decrease", "testing")
            run_exp(12, 4, 15, "decrease", "testing")
            run_exp(4, 12, 15, "decrease", "testing")
            run_exp(4, 36, 15, "decrease", "testing")
            run_exp(36, 4, -15, "decrease", "testing")
            run_exp(36, 4, 15, "decrease", "testing")
            run_exp(36, 12, -15, "decrease", "testing")
            run_exp(12, 4, 15, "decrease", "testing")
            run_exp(36, 12, 15, "decrease", "testing")
            run_exp(12, 4, -15, "decrease", "testing")
            run_exp(12, 36, 15, "decrease", "testing")
            run_exp(4, 36, -15, "decrease", "testing")
            run_exp(12, 36, -15, "decrease", "testing")
            run_exp(36, 4, 15, "decrease", "testing")
            run_exp(4, 12, 15, "decrease", "testing")
            run_exp(4, 36, 15, "decrease", "testing")
            run_exp(36, 4, -15, "decrease", "testing")
            run_exp(36, 12, 15, "decrease", "testing")
            run_exp(12, 4, -15, "decrease", "testing")
            run_exp(36, 12, 15, "decrease", "testing")
            run_exp(36, 12, -15, "decrease", "testing")
            run_exp(4, 36, -15, "decrease", "testing")
            run_exp(12, 36, -15, "decrease", "testing")
            run_exp(36, 4, 15, "decrease", "testing")
            run_exp(36, 12, -15, "decrease", "testing")
            run_exp(4, 36, 15, "decrease", "testing")
            run_exp(36, 4, -15, "decrease", "testing")
            run_exp(36, 12, 15, "decrease", "testing")
            run_exp(12, 4, -15, "decrease", "testing")
            run_exp(36, 4, 15, "decrease", "testing")
            run_exp(12, 4, -15, "decrease", "testing")
            run_exp(12, 36, 15, "decrease", "testing")
            run_exp(4, 36, -15, "decrease", "testing")
            run_exp(12, 36, -15, "decrease", "testing")
            run_exp(36, 4, 15, "decrease", "testing")
            run_exp(36, 12, -15, "decrease", "testing")
            run_exp(4, 12, -15, "decrease", "testing")
            run_exp(12, 4, 15, "decrease", "testing")
            run_exp(36, 4, -15, "decrease", "testing")
            run_exp(36, 4, -15, "decrease", "testing")
            run_exp(12, 4, 15, "decrease", "testing")
            run_exp(36, 12, -15, "decrease", "testing")
            run_exp(36, 12, 15, "decrease", "testing")
            run_exp(12, 4, -15, "decrease", "testing")
            run_exp(4, 12, -15, "decrease", "testing")
            run_exp(4, 12, 15, "decrease", "testing")

  
    def ask_underst():
        ask_message.draw()
        mywin.flip()
        timer = core.Clock()
        thisResp=None
        allKeys=[]
        while thisResp==None :
            allKeys=event.waitKeys(30, 'y, n, a, escape, q', timeStamped=timer) 
            if allKeys:
                for thisKey in allKeys:
                    unders = thisKey[0]
                    mywin.flip()
                    core.wait(1)
                    return unders

    
    training()
    unders = ask_underst()
    if unders == "y":
        testing()            
    if unders == "n":
        training()
        unders = ask_underst()
        if unders == "y":
            testing()
        
 
    # add two more of each
    dataFile.close()
    
    # close and quit
    mywin.close()
    #core.quit()
    
    
