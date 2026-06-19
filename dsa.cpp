
// bugun 19.07.2026 dan boshlab qo'ldan kelgancha c++ da ham ishlab turaman
// switch tanlashdan boshladim c++ dastur exdan


#include <iostream>
using namespace std;

int main(){
    int kun;
    cout<<"Kun raqamini kiriting: ";
    cin>>kun;

    switch (kun){
        case 1:
            cout<<"Dushanba"<<endl;
            break;
        case 2:
            cout<<"Seshanba"<<endl;
            break;
        case 3:
            cout<<"Chorshanba"<<endl;
            break;
        case 4:
            cout<<"Payshanba"<<endl;
            break;
        case 5:
            cout<<"Juma"<<endl;
            break;
        case 6:
            cout<<"Shanba"<<endl;
        case 7:
            cout<<"Yakshanba"<<endl;
            break;
        default:
            cout<<"Bunday hafta kuni yo'q";
    }
    return 0;
}
    









