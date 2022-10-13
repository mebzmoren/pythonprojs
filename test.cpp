#include <iostream>
#include <algorithm>
#include <math.h>

using namespace std;

int main(){
    int number,i, j, d, e, in, k, n, r, sum, Bin1, Bin2, Result1, Result2;

    cout << "Enter the total number of data: " << endl;
    cin >> number;
    int data[number];
    cout << endl;

    cout << "Enter the values separated by a space: " << endl;
    
    for(i=0; i<number; i++){
        cin >> data[i];
    }

    sort(data, data+number);
    cout << endl;

    while(true){
        cout << "Binning Methods " << endl;
        cout << "1. Equal Frequency Binning" << endl;
        cout << "2. Equal Width Binning" << endl;
        cout << "3. Exit" << endl << endl;
        cout << "Enter chosen binning method: " << endl;
        cin >> in;

        if(in==1){
            cout << "Enter the depth of bin: " << endl;
            cin >> d;
            cout << endl;

            e = number / d;
            int b[e][d], avg[e], mean[e][d];
            k = 0;

            for(i=0; i<e; i++){
                cout << "BIN " << (i+1) << ": ";
                
                for(j=0; j<d; j++){
                    b[i][j] = data[j+k];
                    cout << b[i][j] << " ";
                }

                k = k + 3;
                cout << endl;
            }

            for(i=0; i<e; i++){
                sum=0;

                for(j=0; j<d; j++){
                    sum = sum + b[i][j];
                }

                avg[i] = sum / d;
            }

            for(i=0; i<e; i++){
                for(j=0; j<d; j++){
                    mean[i][j] = avg[i];
                }
            }

            cout << "Bin using mean method: " << endl;

            for(i=0; i<e; i++){
                cout << "BIN " << (i+1) << ": ";

                for(j=0; j<d; j++){
                    cout << mean[i][j] << " ";
                }

                cout << endl;
            }

            cout << "Bin using boundary method: " << endl;

            for(i=0; i<e; i++){
                Bin1 = b[i][0];
                Bin2 = b[i][d-1];

                for(j=0; j<d; j++){
                    if(abs(b[i][j] - Bin1) < abs(b[i][j] - Bin2)){
						b[i][j] = Bin1;
					}
					
                    else if(abs(b[i][j] - Bin1) > abs(b[i][j] - Bin2)){
                        b[i][j] = Bin2;
                    }

                    else{
                        b[i][j] = Bin1;
                    }
                }
            }

            for(i=0; i<e; i++){
                cout << "BIN " << (i+1) << ": ";
                
                for(j=0; j<d; j++){
                    cout << b[i][j] << " ";
                }

                cout << endl;
            }
        }

        else if(in == 2){
            for(i=0; i<n; i++){
                cout << data[i] ;
            }

            cout << endl;
            cout << "Please Enter the numberber of bins: " << endl;
            cin >> n;

            int w[n][number], bw[n][number], count1[n], z, n1;
            r = (data[n-1] - data[0]) / n;
            Result1 = data[0];
            Result2 = Result1 + r;

            for(i=0; i<n; i++){
                z = 0;
                cout << "BIN " << (i+1) << ": ";

                for(j=0; j<number; j++){
                    if((Result1 <= data[j]) && (data[j] <= Result2)){
                        w[i][j] = data[j];
                        z = z + 1;
                        cout << w[i][j] << " ";
                        count1[i] = z;
                    }

                    else{
                        w[i][j] = 0;
                    }
                }

                Result1 = Result1 + r + 1;
                Result2 = Result2 + r;

                cout << endl;

            }
        }

        else if(in == 3){
            exit(0);
        }
    }

    return 0; 
}
