import java.io.BufferedReader;
import java.io.FileReader;
import java.io.IOException;
import java.util.Scanner;

public class A {

    public static void main(String[] args) {

        Scanner leitor = new Scanner(System.in);
        System.out.println("Digite a sigla do estado: ");
        String sigla = leitor.nextLine();
        leitor.close();

        try {

            FileReader arq = new FileReader("UF.csv");
            BufferedReader lerArq = new BufferedReader(arq);

            String linha = lerArq.readLine();
            Boolean achou = false;

            while (linha.length() > 0) {
                String[] estadoInfo = linha.split(",");

                if (estadoInfo[1].equalsIgnoreCase(sigla)) {
                    
                    achou = true;
                    String nome = estadoInfo[2];
                    String regiao = "";

                    switch (estadoInfo[3]) {
                        case "1":
                            regiao = "Norte";
                            break;
                        case "2":
                            regiao = "Nordeste";
                            break;
                        case "3":
                            regiao = "Sudeste";
                            break;
                        case "4":
                            regiao = "Sul";
                            break;
                        case "5":
                            regiao = "Centro Oeste";
                            break;
                    }

                    System.out.println("Estado: " + nome + ". Região: " + regiao);
                    break;

                } else {
                    linha = lerArq.readLine();
                }

            }

            arq.close();

            if (!achou) {
                System.out.println("Estado não encontrado.");
            }

        } catch (IOException e) { 
            System.err.println("Erro na abertura do arquivo: " + e.getMessage());
        }

    }

}
