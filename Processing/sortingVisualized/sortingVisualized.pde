static ArrayList<int[]> steps = new ArrayList(); //<>//
int iter = 0;
int size = 100;
float[] unsorted = randomgen(size, 100);
float maxht = 0;
float[][] rectsz = new float[size][2];
int[][] colz = new int[size][3];

float rectWdth = 0;

// 0 = selection area [0,start,stop] , 1 = swap vals [1,pos1,pos2] * 2, 2 = merge area[2,start1,end1,start2,end2], 3 = counter[3,counter1,counter2], 4 = pivot

//[?,color] color - 0= grey, 1 = blue, 2 = red, 3 = green,4 =yellow,5 = black ? = value
public static float[] merge(float[] a, float[] b, int startIndx, ArrayList<int[]> steps1) {
  float[] merged = new float[a.length + b.length];
  int counta = 0;
  int countb = 0;
  for (int i =0; i<merged.length; i++) {
    int[] process = {2, startIndx, startIndx+a.length, startIndx+a.length, startIndx+b.length};
    steps1.add(process);
    if (counta >= a.length) {
      merged[i] = b[countb];
      countb++;

    } else if (countb >= b.length) {
      merged[i] = a[counta];
      counta++;
    } else if (a[counta]<b[countb]) {
      merged[i] = a[counta];
      counta++;
      //int[] process1 = {1, startIndx+counta, startIndx+a.length+countb-1};
      //steps1.add(process1);
      //int[] process2 = {1, startIndx+counta, startIndx+a.length+countb-1};
      //steps1.add(process2);
    } else if (b[countb]<a[counta]) {
      merged[i] = b[countb];
      countb++;
      int[] process1 = {1, startIndx+a.length+countb-1,startIndx+counta};
      steps1.add(process1);
      int[] process2 = {1, startIndx+a.length+countb-1,startIndx+counta};
      steps1.add(process2);
    }
  }

  return merged;
}

static float[] sort(float[] a, int len, int stindx, ArrayList<int[]> steps1) {
  int[] process = {0, stindx, stindx+len-1, 0, 0, 0, 0};
  steps1.add(process);
  if (len <= 1) {
    return a;
  }
  int mid = len/2;
  float[] parta = subset(a, 0, mid);
  float[] partb = subset(a, mid, len-mid);



  return merge(sort(parta, mid, stindx, steps1), sort(partb, len-mid, stindx+mid, steps1), stindx, steps1);
  //return merge(sort(parta, parta.length), sort(partb, partb.length));
}

float[] randomgen(int len, float maxsize) {
  float[] ret = new float[len];
  for (int i =0; i<len; i++) {
    ret[i]= random(maxsize);
  }

  return ret;
}

void setup() {

  float[] sorted = sort(unsorted, size, 0, steps);
  //println(steps);
  //frameRate(6000);
  size(1200, 1000);
  println("Done");
  //println(sorted);
  for (int i =0; i<sorted.length; i++) { //<>//
    float[] tmp = {unsorted[i], 0};
    rectsz[i] =tmp; 
  }
  maxht = sorted[sorted.length-1];
  rectWdth = float(width-(width/32))/sorted.length;
}

float[][] selectionarea(float[][] rects, int start, int stop) {
  println("Changing..");
  for (int i =0; i<rects.length; i++) {
    if (i >= start && i <= stop) {
      rects[i][1] = 2.0;
      println(rects[i][1]);
    } else {
      //println("Hi");
      rects[i][1] = 0.0;
    }
  }
  return rects;
}


float[][] counters(float[][] rects, int count1, int count2) {
  for (int i =0; i<rects.length; i++) {
    if ((i >= count1 || i <= count2)) {
      rects[i][1] = 1;
    }
  }
  return rects;
}

float[][] swapvals(float[][] rects, int pos1, int pos2) {
  if (rects[pos1][1] == 3 && rects[pos2][1] == 3) {
    float[] tmp = rects[pos2];
    rects[pos2] = rects[pos1];
    rects[pos1] = tmp;
    rects[pos1][1] = 0;
    rects[pos2][1] = 0;
  } else {
     rects[pos1][1] = 3;
     rects[pos2][1] = 3;
  }
  return rects;
}


float[][] mergeArea(float[][] rects, int start1, int stop1, int start2, int stop2) {
  for (int i =0; i<rects.length; i++) {
    if ((i >= start1 && i <= stop1)) {
      rects[i][1] = 4;
    }else if((i >= start2 && i <= stop2)){
      rects[i][1] = 6;
    
    } else {
      rects[i][1] = 0;
    }
  }
  return rects;
}
// 0 = selection area [0,start,stop] , 1 = swap vals [1,pos1,pos2] * 2, 2 = merge area[2,start1,end1,start2,end2], 3 = counter[3,counter1,counter2], 4 = pivot
float[][] changedata(float[][] rects, int[][] cols, int[] step) {
  switch(step[0]) {
  case 0:
    return selectionarea(rects, step[1], step[2]);
  case 1:
    return swapvals(rects, step[1], step[2]);
  case 2:
    //println(step);
    return mergeArea(rects, step[1], step[2], step[3], step[4]);
  case 3: 
    return counters(rects, step[1], step[2]);
  }
  return null;
}


void draw() {
  background(220,220,220);
  //println("hi" + iter); //<>//
  float rectHeight;
  for (int val =0; val < rectsz.length; val++) {
    rectHeight = (rectsz[val][0]/maxht)*(height-100);
    //println((rectWdth*val)+20 + " " + maxht);
    //int[] xz = colz[val];
    //println(xz);
    float x = rectsz[val][1];
    if(x == float(1)){
      fill(255,255,255);
      //println(x);
    
    }else if(x == float(0)){
       fill(0,0,0);
       //println(x);
    }
    else if(x == float(2)){
       fill(0,255,0);
    }
    else if(x == float(3)){
       fill(0,0,255);
    }else if(x == float(4)){
       fill(0,255,255);
    }else if(x == float(5)){
       fill(155,255,155);
    }else if(x == float(6)){
       fill(155,50,155);
    }
    //println(rectWdth);
    rect((rectWdth*val)+(width/64), height-30, rectWdth, -rectHeight);
    fill(0,0,0);
  }

    if (iter <= steps.size()) {
    int[] tmp = steps.get(iter);
    println(tmp);
      rectsz = changedata(rectsz, colz, steps.get(iter)); //<>//
  } 
  iter++;
}