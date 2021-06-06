int amplitude = 200;
int wavespeed = 100;
float ballpos;
int framerate = 60;
int waveDensity = 300;
float cur=0;


void setup(){
    size(1000, );
    frameRate(framerate);
  }
  
void draw(){
   background(102);
   for(int i =0; i < waveDensity;i++ ){
     float yval = sin(cur+i*(width/wavespeed))*(amplitude/2) ;
     float xval = i*(width/wavespeed)+(width/wavespeed)*2;
     ellipse(xval,yval+ (height/2),10,10);
     float r = 220;
     float g = 255*((255)*(xval/width));
     float b = 255*((255/amplitude)*yval/amplitude);
     fill(r,g,b);
     print(yval+"\n");

   }
   cur+=0.2;
   if(cur >=360){
   cur = 0;
   }
}

float calcpos(float pos,float ballmultiplier,int i){
  return 1.2;
}