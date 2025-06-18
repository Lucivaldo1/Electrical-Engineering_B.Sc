#include <iostream>
#include <string>
#include <vector>
#include <locale>
#include <stdlib.h>
#include"autoLatex.cpp"


using namespace std;

int main(){
	
	setlocale(LC_ALL, "portuguese");
	
	
	Auto texto;
	
	int colunas, linhas, option;
	
	string elemento, titulo, fonte, label, figura, nomeArquivo, unidadeAcademica, laboratorio, continuar = "s";

	while(continuar == "s" | continuar == "S" ){
	
		texto.printMenu();
		cin >> option;
		switch(option){
			case 1:
				
				cout << "Digite o título do experimento: ";
				fflush(stdin);
				getline(cin, titulo);
				texto.setTitulo(titulo);
				system("cls");
				texto.printCapa();
				break;
			
			case 2:
				
				cout <<"Digite o título da tabela: ";
				fflush(stdin);
				getline(cin,titulo);
				texto.setTitulo(titulo);
			
				
				cout <<"Digite a fonte dos dados da tabela: ";
				fflush(stdin);
				getline(cin,fonte);
				texto.setFonte(fonte);
			
				cout <<"Digite a tag da tabela (referência cruzada): ";
				fflush(stdin);
				getline(cin,label);
				texto.setLabel(label);
			
				cout << "Digite o número de linhas: ";
				cin >> linhas;
				texto.setLinhas(linhas);
			
				cout << "Digite o número de colunas: ";
				cin >> colunas;
				
				texto.setColunas(colunas);
			
			
				texto.fillTable(elemento);
			
				system("cls");
			
				texto.printTable();
			
				break;
				
			case 3:
				
				cout << "Digite o título da figura: ";
				fflush(stdin);
				getline(cin, figura);
				texto.setFigura(figura);
				
				cout <<"Digite a fonte da figura: ";
				fflush(stdin);
				getline(cin, fonte);
				texto.setFonte(fonte);
				
				cout <<"Digite o nome do arquivo: ";
				fflush(stdin);
				getline(cin, nomeArquivo);
				texto.setNomeArquivo(nomeArquivo);
				
				cout <<"Digite a tag da figura (referência cruzada): ";
				fflush(stdin);
				getline(cin,label);
				texto.setLabel(label);
				
				system("cls");
				
				texto.printFigura();
				
				break;
			case 4:
				system("cls");
				texto.printCitacao();
				break;
			case 0:
				cout<<"Você escolheu sair.";
				return 1;
				break;
		}
	cout << "Deseja continuar? (s/n) ";
	cin >> continuar;
	
	system("cls");
	
}
	return 0;
}




