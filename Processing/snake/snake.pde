import processing.sound.*;
SoundFile music;
SoundFile bing;
int framerate = 60;
int speed = 10;
int size = 10;
int curspeedx = speed;
int curspeedy = 0;
int posx = 10;
int posy = 10;
int slen = 5; 

int[] food = {int(random(0,speed))*(int(width/speed)),int(random(0,speed))*(int(width/speed))};
ArrayList<int[]> pos = new ArrayList<int[]>();

void setup () {
  frameRate(10);
  size(500,500);
  music = new SoundFile(this, "music.mp3");
  bing = new SoundFile(this, "bing.mp3");
  music.amp(0.25);
  music.loop();

  
}


void draw()
{
  background(0,0,0);
  keychecker();
  posx += curspeedx;
  posy += curspeedy;
  int[] head = {posx,posy};
  if(pos.size() > slen){
    pos.remove(0);
  }
  pos.add(head);
  if(posx > width){
      posx = 0;
  }
  if(posy > height){
      posy = 0;
  }
  if(posx < 0){
      posx = width;
  }
  if(posy < 0){
      posy = height;
  }
  
  printArray(food);
  fill(255,0,0);
  ellipse(food[0],food[1],size,size);
  fill(255,255,255);
  for(int i =0;i<pos.size();i++)
  {
    int[] cur = pos.get(i);
    if(i != pos.size()-1 && equ( cur , head)){
        speed = 10;
        curspeedx = speed;
        curspeedy = 0;
        posx = 10;
        posy = 10;
        slen = 5; 
        pos = new ArrayList<int[]>();
    
    }
    if(equ(cur,food)){
     slen+=1;
     int[] temp = {int(random(0,speed))*(int(width/speed)),int(random(0,speed))*(int(width/speed))};
      arrayCopy(temp,food);
      music.amp(0.1);
      bing.amp(0.1);
      bing.play();
      music.amp(0.25);
    }
    
    ellipse(cur[0],cur[1],size,size);

  }
  

  
  /**
  for(int i =0;i<slen;i++){
    
    int xadd = 0;
    int yadd = 0;
    if(curspeedx > 0){
      xadd = (i*20);
    }
    else if(curspeedx < 0){
      xadd = -(i*20);
    }
    if(curspeedy > 0){
      yadd = (i*20);
    }
    else if(curspeedy < 0){
      yadd = -(i*20);
    }
    
    ellipse(posx-xadd,posy-yadd,20,20);
    //ellipse(posx,posy,20,20);
  }
**/
  
  
}

boolean equ(int[] one, int[] two){
  for(int i =0;i<2;i++){
    if(one[i] != two[i]){return false;}
  
  }
return true;

}
void keychecker(){

if (keyPressed) {
    if (key == 'w' || key == 'W' || keyCode == UP) {
      if(curspeedy <= 0){
      curspeedx = 0;
      curspeedy = -speed;
      }
    }else if(key == 's' || key == 'S'|| keyCode == DOWN){
            if(curspeedy >= 0){
      curspeedx = 0;
      curspeedy = speed;
      }

    }else if(key == 'd' || key == 'D'|| keyCode == RIGHT){
            if(curspeedx >= 0){
      curspeedx = speed;
      curspeedy = 0;
      }

    }else if(key == 'a' || key == 'A'|| keyCode == LEFT){
            if(curspeedx <= 0){
      curspeedx = -speed;
      curspeedy = 0;
      }
    }else if(key == 'b' || key == 'b'){
        slen+=1;
    }
    
}
}