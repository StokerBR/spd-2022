import java.sql.SQLException;
import java.util.List;

public class ListarCandidato {

    public static void listar() throws SQLException {

        CandidatoDAO dao = new CandidatoDAO();

        System.out.println(String.format("%-10s %-35s %-10s %-20s %-20s %-20s", "Código", "Nome", "Sexo", "Data Nascimento", "Cargo Pretendido", "Curriculo"));
        List<Candidato> candidatos = dao.listar();
        candidatos.forEach(c -> {
            System.out.println(String.format("%-10s %-35s %-10s %-20s %-20s %-20s", c.codigo, c.nome, c.sexo, c.dataNasc, c.cargoPretendido, c.textoCurriculo));
        });
        
    }

}
