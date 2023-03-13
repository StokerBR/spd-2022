import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.SQLException;

public class FabricaConexao {

    public static Connection obterConexao() throws SQLException {
        Connection con = DriverManager.getConnection("jdbc:postgresql://localhost:5432/spd?stringtype=unspecified", "postgres", "postgres");
        return con;
    }

}
