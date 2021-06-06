int sheight = 5;
int g = 2;
float ballpos;
int framerate = 60;
int ballamt = 100;
float[] ypos = new float[ballamt];
float[] multplr = new float[ballamt];


void setup(){
    for(int i =0;i<multplr.length;i++){multplr[i]=random(0,2);}
    size(640, 360);
    frameRate(framerate);
    printArray(ypos);
  }
  
void draw(){
   background(102);
   for(int i =0; i<ballamt;i++){
          ellipse(10+(640/ballamt)*i, int(ypos[i]),40, 40);
          ypos[i] = calcpos(ypos[i],multplr[i],i);
   }
}

float calcpos(float pos,float ballmultiplier,int i){
  ballmultiplier += 1 + (1/framerate);
  print(" Multiplier = " +ballmultiplier + "\n");
  pos += ballmultiplier*g;
  print("Pos = "+pos);
  if(pos>360-40){
    ballmultiplier = ballmultiplier* -1; 
    fill(random(0,255),random(0,255),random(0,255));
  }
  multplr[i] = ballmultiplier;
  return pos;
}