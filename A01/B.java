import java.io.DataOutputStream;
import java.io.FileOutputStream;
import java.io.IOException;
import java.util.Scanner;

public class B {
 
    public static void main(String[] args) {

        Scanner leitor = new Scanner(System.in);
        
        String nome;
        int idade;
        double salario;
        
        String continuar;
        
        try {
            
            FileOutputStream arquivo = new FileOutputStream("pessoas.dat");
            DataOutputStream gravarArq = new DataOutputStream(arquivo);

            while (true) {

                System.out.println("Informe o nome:");
                nome = leitor.nextLine();
        
                System.out.println("Informe a idade: ");
                idade = leitor.nextInt();
        
                System.out.println("Informe o salário: ");
                salario = leitor.nextDouble();
                
        
                gravarArq.writeUTF(nome);
                gravarArq.writeInt(idade);
                gravarArq.writeDouble(salario);
        
                System.out.println("Deseja inserir mais registros? (s/n)");
                leitor.nextLine();
                continuar = leitor.nextLine();
                
                if (continuar.equalsIgnoreCase("s")) {
                    continue;
                } else {
                    arquivo.close();
                    System.out.println("\nDados gravados com sucesso.\n");
                    break;
                }

            }
            
        } catch (IOException e) { 
            System.err.println("Erro: " + e.getMessage());
        }

        leitor.close();

    }

}
