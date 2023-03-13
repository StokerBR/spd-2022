import java.sql.Connection;
import java.sql.PreparedStatement;
import java.sql.ResultSet;
import java.sql.SQLException;
import java.util.ArrayList;
import java.util.List;

public class CandidatoDAO {
    
    private Connection con;

    public CandidatoDAO() throws SQLException {
        this.con = FabricaConexao.obterConexao();
    }

    public void inserir(Candidato cand) {
        String sql = "INSERT INTO candidato (codigo, nome, sexo, data_nasc, cargo_pretendido, texto_curriculo) VALUES (?, ?, ?, ?, ?, ?)";
        try {
            PreparedStatement instrucao = con.prepareStatement(sql);
            instrucao.setInt (1, cand.codigo);
            instrucao.setString(2, cand.nome);
            instrucao.setString (3, cand.sexo);
            instrucao.setString (4, cand.dataNasc);
            instrucao.setString (5, cand.cargoPretendido);
            instrucao.setString (6, cand.textoCurriculo);
            instrucao.execute();
        } catch (SQLException e) {
            System.err.println("Erro durante a inserção dos dados!");
            System.err.println(e);
        }
    }

    public List<Candidato> listar() {
        List<Candidato> listaDeCandidatos = new ArrayList<Candidato>();
        String sql = "SELECT codigo, nome, sexo, data_nasc, cargo_pretendido, texto_curriculo FROM candidato ";

        try {

            PreparedStatement instrucao = con.prepareStatement(sql);
            ResultSet resultado = instrucao.executeQuery();

            while (resultado.next()) {

                Candidato c = new Candidato(
                    resultado.getInt("codigo"),
                    resultado.getString("nome"),
                    resultado.getString("sexo"),
                    resultado.getString("data_nasc"),
                    resultado.getString("cargo_pretendido"),
                    resultado.getString("texto_curriculo")
                );

                listaDeCandidatos.add(c);
                
            }

        } catch (SQLException e) {
            System.err.println("Erro durante a busca dos dados!");
        }

        return listaDeCandidatos;

    }

}
