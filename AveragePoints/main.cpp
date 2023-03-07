//
// Created by Oskar Paśko on 07/03/2023.
//
#include <iostream>
using namespace std;

int main()
{
    int points = 0;
    cout<<"Podaj maksymalną liczbę punktów: "; cin>>points;

    for(int x=0;x<points+1;x++)
    {
        if(((x/points)*100) >=0 && ((x/points)*100)<30) cout<<"1 = "<<x<<"pkt"<<endl;
        if(((x/points)*100) >=30 && ((x/points)*100)<35) cout<<"-2 = "<<x<<"pkt"<<endl;
        if(((x/points)*100) >=35 && ((x/points)*100)<43) cout<<"2 = "<<x<<"pkt"<<endl;
        if(((x/points)*100) >=43 && ((x/points)*100)<47) cout<<"+2 = "<<x<<"pkt"<<endl;
        if(((x/points)*100) >=47 && ((x/points)*100)<50) cout<<"-3 = "<<x<<"pkt"<<endl;
        if(((x/points)*100) >=50 && ((x/points)*100)<63) cout<<"3 = "<<x<<"pkt"<<endl;
        if(((x/points)*100) >=63 && ((x/points)*100)<69) cout<<"+3 = "<<x<<"pkt"<<endl;
        if(((x/points)*100) >=69 && ((x/points)*100)<75) cout<<"-4 = "<<x<<"pkt"<<endl;
        if(((x/points)*100) >=75 && ((x/points)*100)<83) cout<<"4 = "<<x<<"pkt"<<endl;
        if(((x/points)*100) >=83 && ((x/points)*100)<87) cout<<"+4 = "<<x<<"pkt"<<endl;
        if(((x/points)*100) >=87 && ((x/points)*100)<90) cout<<"-5 = "<<x<<"pkt"<<endl;
        if(((x/points)*100) >=90 && ((x/points)*100)<=100) cout<<"5 = "<<x<<"pkt"<<endl;
        if(x<points)
        {
            if((((x+0.5)/points)*100) >=0 && (((x+0.5)/points)*100)<30) cout<<"1 = "<<x+0.5<<"pkt"<<endl;
            if((((x+0.5)/points)*100) >=30 && (((x+0.5)/points)*100)<35) cout<<"-2 = "<<x+0.5<<"pkt"<<endl;
            if((((x+0.5)/points)*100) >=35 && (((x+0.5)/points)*100)<43) cout<<"2 = "<<x+0.5<<"pkt"<<endl;
            if((((x+0.5)/points)*100) >=43 && (((x+0.5)/points)*100)<47) cout<<"+2 = "<<x+0.5<<"pkt"<<endl;
            if((((x+0.5)/points)*100) >=47 && (((x+0.5)/points)*100)<50) cout<<"-3 = "<<x+0.5<<"pkt"<<endl;
            if((((x+0.5)/points)*100) >=50 && (((x+0.5)/points)*100)<63) cout<<"3 = "<<x+0.5<<"pkt"<<endl;
            if((((x+0.5)/points)*100) >=63 && (((x+0.5)/points)*100)<69) cout<<"+3 = "<<x+0.5<<"pkt"<<endl;
            if((((x+0.5)/points)*100) >=69 && (((x+0.5)/points)*100)<75) cout<<"-4 = "<<x+0.5<<"pkt"<<endl;
            if((((x+0.5)/points)*100) >=75 && (((x+0.5)/points)*100)<83) cout<<"4 = "<<x+0.5<<"pkt"<<endl;
            if((((x+0.5)/points)*100) >=83 && (((x+0.5)/points)*100)<87) cout<<"+4 = "<<x+0.5<<"pkt"<<endl;
            if((((x+0.5)/points)*100) >=87 && (((x+0.5)/points)*100)<90) cout<<"-5 = "<<x+0.5<<"pkt"<<endl;
            if((((x+0.5)/points)*100) >=90 && (((x+0.5)/points)*100)<=100) cout<<"5 = "<<x+0.5<<"pkt"<<endl;
        }
    }
}