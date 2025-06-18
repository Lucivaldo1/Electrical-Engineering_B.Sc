#ifndef AUTOLATEX_H
#define AUTOLATEX_H
using namespace std;
class Auto{
	
	private:
		int colunas, linhas;

		string elemento, titulo, fonte, label, capa, figura, nomeArquivo, unidadeAcademica, laboratorio;
	public:
		
		Auto(); // construtor
		//set (tabela)
		
		
		void setColunas(int colunas);
		
		void setLinhas(int linhas);
		
		void setElemento(string elemento);
		
		void setTitulo(string titulo);
		
		void setFonte(string fonte);
		
		void setLabel(string label);
		
		//set (figura)
		
		void setFigura(string figura);
		
		void setNomeArquivo(string nomeArquivo);
		
		//o setFonte() será utilizado aqui também (talvez haja herança em futuro próximo.
		
		//set (capa)
			
		void setCapa();
		
		void setUnidadeAcademica(string unidadeAcademica);
		
		void setLaboratorio(string laboratorio);
		
		//get
		
		int getColunas();
		
		int getLinhas();
		
		string getElemento();
		
		string getTitulo();
		
		string getFonte();
		
		string getLabel();
		
		//figura
		
		string getFigura();
		
		string getNomeArquivo();
		
		//get(capa)
		
		string getUnidadeAcademica();
		
		string getLaboratorio();
		
		//outro (tabelas)
		
		void fillTable(string elemento);
		
		void printTable();
		
		//outro (capa)
		
		void printCapa();
		
		//outro (figura)
		
		void printFigura();
		
		//menu
		
		
		void printMenu();
		
		// citação longa
		
		void printCitacao();
};

#endif
