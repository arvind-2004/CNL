import java.net.*;
import java.io.*;

class MyClient1 {
    public static void main(String args[]) {
        try {
            Socket s = new Socket("localhost", 3333);
            DataInputStream din = new DataInputStream(s.getInputStream());
            DataOutputStream dout = new DataOutputStream(s.getOutputStream());
            BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

            String str = "", str2 = "";
            while (!str.equals("stop")) {
                System.out.print("Enter message for server: ");
                str = br.readLine();
                dout.writeUTF(str);
                dout.flush();
                str2 = din.readUTF();
                System.out.println("Server says: " + str2);
            }

            // Close resources
            br.close();
            din.close();
            dout.close();
            s.close();

        } catch (Exception e) {
            e.printStackTrace();
        }
    }
}
