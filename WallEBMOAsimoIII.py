 #BEGIN CODE FOR DANCE OFF
    
    def _gopigo3_command_dance_off(self):
        beat = 60/130
        s = 1000
        
        self.gopigo3.set_speed(s)
        
      
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
        self.gopigo3.spin_right()
        sleep(1.25*beat)
        self.gopigo3.drive_cm(3)
        sleep(0.5*beat)
        self.gopigo3.drive_cm(3)
        sleep(0.5*beat)
        
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
        sleep(4*beat)
        
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
        sleep(2.5*beat)
        
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
        sleep(2.35*beat)
        
        
        self.gopigo3.drive_cm(5)
        sleep(1.35*beat)
        self.gopigo3.drive_cm(3)
        sleep(0.5*beat)
        self.gopigo3.drive_cm(3)
        sleep(0.5*beat)
        self.gopigo3.drive_cm(3)
        sleep(1.25*beat)
        self.gopigo3.spin_left()
        sleep(2.35*beat)
        
        
        self.gopigo3.drive_cm(5)
        sleep(1.35*beat)
        self.gopigo3.drive_cm(3)
        sleep(0.5*beat)
        self.gopigo3.drive_cm(3)
        sleep(0.5*beat)
        self.gopigo3.drive_cm(3)
        sleep(0.5*beat)
        self.gopigo3.spin_left()
        sleep(2.35*beat)
        
        
        self.gopigo3.drive_cm(5)
        sleep(1.35*beat)
        self.gopigo3.drive_cm(3)
        sleep(0.5*beat)
        self.gopigo3.drive_cm(3)
        sleep(0.5*beat)
        self.gopigo3.drive_cm(3)
        sleep(1.25*beat)
        self.gopigo3.spin_left()
        sleep(2.35*beat)
        

        self.gopigo3.stop()
        sleep(0.75*beat)
        self.gopigo3.spin_right()
        sleep(3*beat)
        self.gopigo3.stop()
        sleep(0.75*beat)
        self.gopigo3.forward()
        sleep(1.5*beat)
        self.gopigo3.backward()
        sleep(1.5*beat)
        self.gopigo3.drive_cm(5)
        sleep(1.35*beat)
        self.gopigo3.drive_cm(3)
        sleep(0.5*beat)
        self.gopigo3.drive_cm(3)
        sleep(0.5*beat)
        self.gopigo3.spin_left()
        sleep(1.5*beat)
        self.gopigo3.spin_right()
        sleep(1.5*beat)
        
        #While Loop Speed Decrease
        while s > 500:
            self.gopigo3.forward()
            sleep(4*beat)
            self.gopigo3.steer(10,s)
            sleep(4*beat)
            s = s - 100
            self.gopigo3.forward()
            sleep(4*beat)
            self.gopigo3.steer(s,10)
            sleep(4*beat)
            s = s - 100
            
        
        #Back to Repeats
        self.gopigo3.drive_cm(5)
        sleep(1.35*beat)
        self.gopigo3.drive_cm(3)
        sleep(0.5*beat)
        self.gopigo3.drive_cm(3)
        sleep(0.5*beat)
        self.gopigo3.drive_cm(3)
        sleep(0.5*beat)
        self.gopigo3.spin_left()
        sleep(2.35*beat)
        
        
        self.gopigo3.drive_cm(5)
        sleep(1.35*beat)
        self.gopigo3.drive_cm(3)
        sleep(0.5*beat)
        self.gopigo3.drive_cm(3)
        sleep(0.5*beat)
        self.gopigo3.drive_cm(3)
        sleep(1.25*beat)
        self.gopigo3.spin_left()
        sleep(2.35*beat)
        
        
        self.gopigo3.drive_cm(5)
        sleep(1.35*beat)
        self.gopigo3.drive_cm(3)
        sleep(0.5*beat)
        self.gopigo3.drive_cm(3)
        sleep(0.5*beat)
        self.gopigo3.drive_cm(3)
        sleep(0.5*beat)
        self.gopigo3.spin_left()
        sleep(2.35*beat)
        
        
        self.gopigo3.drive_cm(5)
        sleep(1.35*beat)
        self.gopigo3.drive_cm(3)
        sleep(0.5*beat)
        self.gopigo3.drive_cm(3)
        sleep(0.5*beat)
        self.gopigo3.drive_cm(3)
        sleep(1.25*beat)
        self.gopigo3.spin_left()
        sleep(2.35*beat)
        self.gopigo3.stop()
        
        
        #START TURNING AROUND THE CIRCLE TO END IN OOPPOOSITE POSITIONS OF WHERE WE STARTED
