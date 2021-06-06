#include <iostream>
#include <cstdlib>
#include <ctime>

using namespace std;
int* getRandom();
int bubbleSort(int* lst);
int* mrge(int* lst1,int* lst2);

const int size = 10000;

int* getRandom( ) {
   //int sz;
   //cout<<"How big list?\n"<<endl;
   //cin >> sz;

   static int  r[size];


   for (int i = 0; i < size; ++i) {
      r[i] = rand();
   }

   return r;
}

int bubbleSort(int* lst){
    while(true){
        bool sorted = true;
        for(int i = 0; i<size;i++){
            if(lst[i]>lst[i+1]){
                int temp = lst[i+1];
                lst[i+1] = lst[i];
                lst[i]=temp;
                sorted = false;
            }

        }

        if(sorted==true){
            break;

        }
    }
    return 0;


}

int* mrge(int* lst1,int* lst2){
    int sz1 = sizeof(lst1);
    int sz2 = sizeof(lst2);
    int tsz = sz1+sz2;
    int nlst[tsz] = {0};
        for(int i = 0;i<20;i++){
        cout<<nlst[i]<<endl;
    }
    int pntr1 = 0;
    int pntr2 = 0;
    bool isDone1 = false;
    bool isDone2 = false;

    for(int i = 0;i<tsz+2;i++){

        cout<<"Lst1:"<<lst1[pntr1]<<" List 2:"<<lst2[pntr2]<<endl;
        if(lst1[pntr1] <lst2[pntr2] && isDone1 == false){

            nlst[i] = lst1[pntr1];
            pntr1 += 1;
        }
        else{
            nlst[i] = lst2[pntr2];
            pntr2 += 1;
        }

        if(pntr1 > sizeof(lst1)){
                isDone1 = true;
           }
        if(pntr2 > sizeof(lst2)){
                isDone2 = true;
           }
    }
    for(int i = 0;i<20;i++){
        cout<<nlst[i]<<endl;
    }

    return nlst;
}


int* quickSort()

int main()
{
    /*int lst1[10] = {1,2,2,3,3,5,9,12,13,17};
    int lst2[10] = {1,70,80,102,399,400,14321,175381,73418971,1031341312};
    int* p;
    p=getRandom();
    mrge(lst1,lst2);*/
    int lst[]={2,4,3,6,5,1}
    //for(int i = 0;i<20;i++){
        //cout << done[1]<<endl;
    //}
    //for(int i=0;i<size;i++){
      //  cout << p[i]<<endl;
    //}


    return 0;
}
