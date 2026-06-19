
// // bugun 19.07.2026 dan boshlab qo'ldan kelgancha c++ da ham ishlab turaman
// // switch tanlashdan boshladim c++ dastur exdan


#include <iostream>
#include<cmath>
#include<cstring>
using namespace std;

// 2

// int main(){
//     int kun;
//     cout<<"Kun raqamini kiriting: ";
//     cin>>kun;

//     switch (kun){
//         case 1:
//             cout<<"Dushanba"<<endl;
//             break;
//         case 2:
//             cout<<"Seshanba"<<endl;
//             break;
//         case 3:
//             cout<<"Chorshanba"<<endl;
//             break;
//         case 4:
//             cout<<"Payshanba"<<endl;
//             break;
//         case 5:
//             cout<<"Juma"<<endl;
//             break;
//         case 6:
//             cout<<"Shanba"<<endl;
//         case 7:
//             cout<<"Yakshanba"<<endl;
//             break;
//         default:
//             cout<<"Bunday hafta kuni yo'q";
//     }
//     return 0;
// }
    



// // 2
// int main(){
//     int k;
//     cout<<"K : ";cin>>k;
//     switch(k){
//         case 1:
//             cout<<"Yomon";
//             break;
//         case 2:
//             cout<<"Qoniqarsiz";
//             break;
//         case 3:
//             cout<<"Qoniqarli";
//             break;
//         case 4:
//             cout<<"Yaxshi";
//             break;
//         case 5:
//             cout<<"Alo";
//             break;
//         default:
//             cout<<"Xato";
//     }
//     return 0;
// }



// // 3

// int main(){
//     int oy;
//     cin>>oy;
//     switch(oy){
//         case 1: case 2: case 3:
//             cout<<"bahor";
//             break;
//         case 4: case 5: case 6:
//             cout<<"yoz";
//             break;
//         case 7: case 8: case 9:
//             cout<<"kuz";
//         case 10: case 11: case 12:
//             cout<<"qish";
//             break;
//         default:
//             break;
//     }
//     return 0;
// }







// // 4
// int main(){
//     int oy;
//     cin>>oy;

//     switch (oy){
//     case 1:
//     case 3:
//     case 5:
//     case 7:
//     case 8:
//     case 10:
//     case 12:
//         cout<<"31 kun";
//         break;
//     case 4:
//     case 6:
//     case 9:
//     case 11:
//         cout<<"30 kun";
//         break;
//     case 2:
//         cout<<"28 yoki 29 kun kabisaga qarab";
//         break;
//     default:
//         cout<<"Bunday kun yo'q";
//         break;
//     }
//     return 0;
// }



// // 5

// int amal() {
//     int a, b;
//     char belgi;

//     cout << "a : "; cin >> a;
//     cout << "b : "; cin >> b;
//     cout << "Amalni kiriting: "; cin >> belgi;
//     switch(belgi) {
//         case '+':
//             return a + b;
//         case '-':
//             return a - b;
//         case '*':
//             return a * b;
//         case '/':
//             if (b != 0) {
//                 return a / b;
//             } else {
//                 cout << "Nolga bo'lish mumkin emas! ";
//                 return 0; 
//             }
//         default: 
//             cout << "Xato amal! ";
//             return 0; 
//     }
// }
// int main() {
//     cout << "javob : " << amal() << endl;
//     return 0;
// }







// // 6

// int main() {
//     int birlik;
//     long double uzunlik, metr;
//     cout << "Birlikni tanlang (1-dm, 2-km, 3-m, 4-mm, 5-cm): ";
//     cin >> birlik;
//     cout << "Kesma uzunligini kiriting: ";
//     cin >> uzunlik;
//     switch(birlik) {
//         case 1: metr = uzunlik / 10.0; break;
//         case 2: metr = uzunlik * 1000.0; break;
//         case 3: metr = uzunlik; break;
//         case 4: metr = uzunlik / 1000.0; break;
//         case 5: metr = uzunlik / 100.0; break;
//         default: 
//             cout << "Noto'g'ri birlik!" << endl; 
//             return 0;
//     }
//     cout << "Metrdagi uzunligi: " << metr << " m" << endl;
//     return 0;
// }








// 7
// double konver() {
//     int birlik;
//     double massa;
//     cout << "Birini tanlang: 1-kg, 2-mg, 3-g, 4-t, 5-sr : "; 
//     cin >> birlik;
//     cout << "Massani kiriting: "; 
//     cin >> massa;
//     switch (birlik) {
//         case 1:
//             return massa;
//         case 2:
//             return massa / 1000000.0; // .0 qo'yish double formatida bo'lishi uvhun
//         case 3:
//             return massa / 1000.0;
//         case 4:
//             return massa * 1000.0;
//         case 5:
//             return massa * 100.0;
//         default:
//             cout << "Xato birlik! ";
//             return 0;
//     }
// }

// int main() {
//     cout << "Javob kg: " << konver() << endl;
//     return 0;
// }




#include<string>

string sana(){
    int day, month, max_day;
    cout<<"Kiriting: Day / month ";cin>>day>>month;
    string kun, oylar[12] = {"yanvar", "fevral", "mart", "aprel", "may", "iyun", "iyul", "avgust", "sentyabr", "oktyabr", "noyabr", "dekabr"};

    switch (month){
    case 1:
    case 3:
    case 5:
    case 7:
    case 8:
    case 10:
    case 12:
        max_day = 31;
    case 4:
    case 6:
    case 9:
    case 11:
        max_day = 30;
    case 2:
        max_day = 28;
    default:
        max_day = 0;
    }
    if (day >= 1 && day <= max_day){
        return to_string(day) + "-" + oylar[month - 1]; 
    }
    else{
        return "Bunday sana mavjud emas!";
    }
}

int main(){
    cout<<sana();
    return 0;
}






















