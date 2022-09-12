 #BEGIN CODE FOR DANCE OFF
    
    def _gopigo3_command_dance_off(self):
        beat = 60/130
        self.gopigo3.set_speed(1000)
      
        #1-4
        self.gopigo3.spin_left()
        sleep(1*beat)
        self.gopigo3.spin_right()
        sleep(2*beat)
        self.gopigo3.spin_left()
        sleep(2*beat)
        self.gopigo3.spin_right()
        sleep(1.3*beat)
       
        #5-7
        self.gopigo3.forward()
        sleep(0.5*beat)
        self.gopigo3.backward()
        sleep(1*beat)
        self.gopigo3.forward()
        sleep(0.5*beat)
        
        #8-11
        self.gopigo3.steer(10,1000)
        sleep(2)
        self.gopigo3.drive_cm(5)
        sleep(1.35*beat)
        self.gopigo3.drive_cm(3)
        sleep(0.5*beat)
        self.gopigo3.drive_cm(3)
        sleep(0.5*beat)
       
        #12-14
        self.gopigo3.spin_left()
        sleep(1.25*beat)
        self.gopigo3.drive_cm(3)
        sleep(0.35*beat)
        self.gopigo3.drive_cm(3)
        sleep(0.35*beat)
        
        #15-21a
        self.gopigo3.spin_left()
        sleep(0.5*beat)
        self.gopigo3.drive_cm(-5)
        sleep(1*beat)
        self.gopigo3.drive_cm(-3)
        sleep(0.5*beat)
        self.gopigo3.drive_cm(-3)
        sleep(0.5*beat)
        self.gopigo3.drive_cm(-3)
        self.gopigo3.steer(1000,10)
        sleep(3*beat)
        self.gopigo3.spin_right()
        sleep(1.2*beat)
        self.gopigo3.stop()
        sleep(3.65*beat)
        
        #22-24
        self.gopigo3.forward()
        sleep(1.15*beat)
        self.gopigo3.backward()
        sleep(1*beat)
        self.gopigo3.forward()
        sleep(1*beat)
        
        #25
        self.gopigo3.spin_right()
        sleep(2.5*beat)
        self.gopigo3.stop()
        sleep(1.5*beat)
        self.gopigo3.forward()
        sleep(2*beat)
        self.gopigo3.backward()
        sleep(2*beat)
        self.gopigo3.spin_right()
        sleep(2.5*beat)
        self.gopigo3.stop()
        sleep(1.5*beat)
        self.gopigo3.backward()
        sleep(2*beat)
        self.gopigo3.forward()
        sleep(2*beat)
        self.gopigo3.spin_right()
        sleep(2.5*beat)
        self.gopigo3.stop()
        sleep(1.5*beat)
        
        self.gopigo3.spin_right()
        sleep(1*beat)
        self.gopigo3.stop()
        sleep(1*beat)
        self.gopigo3.forward()
        sleep(1*beat)
        self.gopigo3.spin_right()
        sleep(1*beat)
        self.gopigo3.stop()
        sleep(0.65*beat)
        self.gopigo3.backward()
        sleep(5*beat)
        self.gopigo3.spin_left()
        sleep(2*beat)
        
        #Repeats Begin
        self.gopigo3.drive_cm(5)
        sleep(1.35*beat)
        self.gopigo3.drive_cm(3)
        sleep(0.5*beat)
        self.gopigo3.drive_cm(3)
        sleep(0.5*beat)
        self.gopigo3.drive_cm(3)
        sleep(0.5*beat)
        self.gopigo3.spin_left()
        sleep(1.25*beat)
        
        
        self.gopigo3.drive_cm(5)
        sleep(1.35*beat)
        self.gopigo3.drive_cm(3)
        sleep(0.5*beat)
        self.gopigo3.drive_cm(3)
        sleep(0.5*beat)
       
        self.gopigo3.spin_left()
        sleep(1.25*beat)
        self.gopigo3.stop()
        sleep(0.75*beat)
        self.gopigo3.spin_right()
        sleep(1.25*beat)
        
        
        #START TURNING AROUND THE CIRCLE TO END IN OOPPOOSITE POSITIONS OF WHERE WE STARTED
