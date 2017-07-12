

try: 
  	import simplegui
except ImportError:
  	import SimpleGUICS2Pygame.simpleguics2pygame as simplegui 

# global variables
counter = 0
tries = 0
success = 0

# helper function converts time
# in tenths of seconds into formatted string A:BC.D
def format(t):    
  	a = (t // 10) // 60    
	b = ((t // 10) % 60) // 10    
	c = ((t // 10) % 60) % 10    
	d = t % 10        
	return str(a) + ":" + str(b) + str(c) + "." + str(d)
  
# event handlers for buttons; "Start", "Stop", "Reset"
def start():    
	global running      
	timer.start()    
	running = True
  
def stop():    
	global success, tries, counter, running    
	timer.stop()    
	if counter % 10 == 0 and running:        
		success += 1    
	if running:        
		tries += 1    
	running = False
	
def reset():    
	global counter, tries, success    
	counter = 0    
	timer.stop()    
	tries = 0    
	success = 0
	
# event handler for timer with 0.1 sec interval
def tick():    
	global counter    
	counter += 1
	
# draw handler
def draw_time(canvas):    
	global counter, tries, success    
	canvas.draw_text(format(counter), [100, 100], 18, 'red')    
	canvas.draw_text(str(tries) + "/" + str(success), [150, 20], 18, 'green')
	
# create frame
f = simplegui.create_frame("Stopwatch Game", 200, 200)

# register event handlers
timer = simplegui.create_timer(100, tick)
f.set_draw_handler(draw_time)
f.add_button("start", start, 100)
f.add_button("stop", stop, 100)
f.add_button("reset", reset, 100)

# start frame
f.start()
