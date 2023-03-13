import java.sql.SQLException;
import java.util.Scanner;

public class IncluirCandidato {

    public IncluirCandidato() {
        
    }

    public static void incluir() throws SQLException {

        Scanner reader = new Scanner(System.in);

        int codigo;
        String nome, sexo, dataNasc, cargoPretendido, textoCurriculo;

        System.out.println("Digite o código do candidato: ");
        codigo = reader.nextInt();
        System.out.println("Digite o nome do candidato: ");
        reader.nextLine();
        nome = reader.nextLine();
        System.out.println("Digite o sexo do candidato (M/F): ");
        sexo = reader.next();
        System.out.println("Digite a data de nascimento do candidato (aaaa-mm-dd): ");
        dataNasc = reader.next();
        System.out.println("Digite o cargo pretendido do candidato: ");
        cargoPretendido = reader.next();
        System.out.println("Digite o curriculo do candidato: ");
        textoCurriculo = reader.next();

        reader.close();

        Candidato candidato = new Candidato(codigo, nome, sexo, dataNasc, cargoPretendido, textoCurriculo);
        CandidatoDAO dao = new CandidatoDAO();
        dao.inserir(candidato);

        System.out.println("Candidato inserido com sucesso!");

    }

}
