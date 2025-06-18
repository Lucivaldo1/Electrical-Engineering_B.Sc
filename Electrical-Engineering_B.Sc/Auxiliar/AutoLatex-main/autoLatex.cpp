#include "autoLatex.h"
#include<locale>
#define matricula 119210605
#define ano 2022


	
vector<vector<string> > v;

Auto::Auto():elemento(""),titulo(""), fonte(""), label(""), capa(""), 
figura(""), nomeArquivo(""), unidadeAcademica(""), laboratorio(""), colunas(0), linhas(0)
{

	
}

//set

void Auto::setColunas(int colunas){
	
	this -> colunas = colunas;
	
}
void Auto::setLinhas(int linhas){
	
	this -> linhas = linhas;
}
		
void Auto::setElemento(string elemento){
	
	this -> elemento = elemento;
}
		
void Auto::setTitulo(string titulo){
	
	this -> titulo = titulo;
}
		
void Auto::setFonte(string fonte){
	
	this -> fonte = fonte;
}
		
void Auto::setLabel(string label){
	
	this -> label = label;
}

void Auto::setFigura(string figura){
	
	this -> figura = figura;
}

void Auto::setNomeArquivo(string nomeArquivo){
	
	this -> nomeArquivo = nomeArquivo;
}

void Auto::setUnidadeAcademica(string unidadeAcademica){
	
	this -> unidadeAcademica = unidadeAcademica;
}
		
void Auto::setLaboratorio(string laboratorio){
	
	this -> laboratorio = laboratorio;
}


//get
int Auto::getColunas(){
	
	return colunas;
}

int Auto::getLinhas(){
	
	return linhas;
}
		
string Auto::getElemento(){
	
	return elemento;
}
		
string Auto::getTitulo(){
	
	return titulo;
}
		
string Auto::getFonte(){
	
	return fonte;
}


string Auto::getLabel(){
	
	return label;
}

string Auto::getFigura(){
	
	return figura;
}

string Auto::getNomeArquivo(){
	
	return nomeArquivo;
}

string Auto::getUnidadeAcademica(){
	
	return unidadeAcademica;
}


string Auto::getLaboratorio(){
	
	return laboratorio;
}

//outro

void Auto::printMenu(){
		cout<<"Desenvolvido por: Lucivaldo Barbosa"<<endl
		<<" _______________________________"<<endl
		<<"| \t\t\t\t|"<<endl
		<<"|Menu de tarefas automatizadas  |"<<endl
		<<"|Opções:\t\t\t|"<<endl
		<<"|1 - Capa de experimento\t|"<<endl
		<<"|2 - Tabela\t\t\t|"<<endl
		<<"|3 - Figura\t\t\t|"<<endl
		<<"|4 - Citação longa\t\t|"<<endl
		<<"|0 - Sair\t\t\t|"<<endl
		<<"| \t\t\t\t|"<<endl
		<<"|_______________________________| "<<endl
		<<"Digite sua opção: ";
}


// esta função preenche o vector a partir das entradas do usuário.
void Auto::fillTable(string elemento){
		//entrada no vector
	for (int i=0; i< getLinhas();i++){
		string entrada;
		vector<string> v2;
		for (int j=0; j< getColunas();j++){
			cout<<"Digite a entrada da linha "<<i+1<<" e da coluna "<<j+1<<" da tabela: ";
			fflush(stdin);
			getline(cin, entrada);
			setElemento(entrada);
			v2.push_back(getElemento());

		}
		v.push_back(v2);
	}

}

void Auto::printTable(){

	//print da tabela
cout<<"%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%% "<<endl;
cout<<"\\begin{table}[h]"<<endl<<endl
	<<"\\caption{"<<getTitulo()<<"}"<<endl
	<<"\\centering"<<endl
	<<"%%opcional\\begin{adjustwidth}{-2cm}{}"<<endl
	<<"\\begin{tabular}{|*{"<<getColunas()<<"}{c|}}";

cout << "\\hline"<<endl;
	for (int i = 0; i < v.size(); i++) {
		
			        for (int j = 0; j < v[i].size(); j++){
	            cout <<"\\thead{" <<v[i][j]<<"}";
	        	if (j < getColunas()-1){
	        		cout << " & ";
	        	}
	      
	        }
	        	
	        cout <<" \\\\ \\hline"<<endl;
	    }

cout<<"\\end{tabular}"<<endl
	<<"\\caption*{Fonte: "<<getFonte()<<"}"<<endl
	<<"%%opcional\\end{adjustwidth}{}"<<endl
	<<"\\label{"<<getLabel()<<"}"<<endl
	<<"\\end{table}" <<endl
	<<"%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%% "<<endl;

	// clean the vector so that you can reuse it without bothering with thrash
	v.clear();
}

void Auto::printCapa(){

	cout<<"%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%"<<endl
 <<"\\documentclass[a4paper,12pt]{article}"<<endl
<<"\\usepackage[brazilian]{babel}"<<endl
<<"\\usepackage[document]{ragged2e}"<<endl
<<"\\usepackage[top=3cm,bottom=2cm,right=2cm,left=3cm]{geometry}"<<endl
<<"\\usepackage[utf8]{inputenc}"<<endl

<<"\\usepackage{amsmath, amssymb, gensymb}"<<endl



<<"\\usepackage{caption} %legenda de tabelas"<<endl
<<"\\usepackage{lmodern}"<<endl
<<"\\usepackage[T1]{fontenc}"<<endl


<<"\\usepackage{graphicx}"<<endl


<<"\\usepackage{lipsum}"<<endl
<<"\\usepackage{setspace} %para setar espaçamento horizontal e vertical%"<<endl
<<"\\usepackage{changepage} %ajuste do tamanho de tabelas e figuras (\\adjustwidth)"<<endl
<<"\\usepackage{makecell} %formatar celulas de uma tabela (\\thead)"<<endl
<<"\\usepackage{quoting} %citação"<<endl
<<"\\usepackage{times} %fonte: times new roman"<<endl



<<"\\begin{document}"<<endl
	
	<<"\\begin{center}"<<endl
		<<"{\\fontsize{18pt}{1.5pt} \\selectfont "<<endl
			<<"Universidade Federal de Campina Grande \\\\"<<endl
			<<"Centro de Ciências e Tecnologia \\\\"<<endl
			<<"Unidade acadêmica de Física\\\\"<<endl
			<<"Laboratório de Física Experimental I\\\\}"<<endl
		
		<<"\\vspace*{\\fill}"<<endl
		<<"{\\fontsize{20pt}{1.5pt} \\selectfont"<<endl
			<<getTitulo()<<endl
			<<"\\vspace*{\\fill}}"<<endl
	<<"\\end{center}"<<endl
	<<"\\mbox{}"<<endl
	<<"\\vfill"<<endl
	<<"{\\fontsize{14pt}{16pt} \\selectfont"<<endl
		<<"Aluno:  \\hspace{1cm} Matrícula: \\\\"<<endl
		<<"Turma:  	\\hspace{1cm} Professor(a):  \\hspace{1cm}	Nota: \\\\"<<endl
		<<"\\begin{center}"<<endl
			<<"Campina Grande, "<<ano<<"."<<endl
		<<"\\end{center}}\\pagebreak"<<endl
			<<"\\pagebreak"<<endl
	<<"\\justifying"<<endl
	<<"\\onehalfspacing"<<endl
	<<"\\setlength{\\parindent}{1.25cm}"<<endl
	<<"\\end{document}"<<endl;

cout<<endl<<endl<<"%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%"<<endl<<endl<<endl;
}


void Auto::printFigura(){
	cout<<"%%%%%%%%%%%%%%%%%%%%"<<endl
		<<"\\begin{figure}[h]"<<endl
		<<"\\centering"<<endl
		<<"\\caption{"<<getFigura()<<"}"<<endl
		<<"\\includegraphics[scale=1]{"<<getNomeArquivo()<<"} %altere o fator da escala para mudar o tamanho da figura"<<endl 
		<<"\\caption*{Fonte: "<<getFonte()<<"}"<<endl
		<<"\\label{"<<getLabel()<<"}"<<endl
		<<"\\end{figure}"<<endl
		<<"%%%%%%%%%%%%%%%%%%%%"<<endl;
}

void Auto::printCitacao(){
	
	cout<<"\\begin{quoting}[rightmargin=0cm,leftmargin=4cm]"<<endl
	<<"\\begin{singlespace}"<<endl
		<<"{\\footnotesize "<<endl
		<<endl	
		<<"	sua citação aqui (AUTOR, ANO, p.xx)."<<endl
		<<"}"<<endl
	<<"\\end{singlespace}"<<endl
<<"\\end{quoting}"<<endl;

}
