/*
 * Origin of the benchmark:
 *     license: 4-clause BSD (see /java/jbmc-regression/LICENSE)
 *     repo: https://github.com/diffblue/cbmc.git
 *     branch: develop
 *     directory: regression/jbmc-strings/StringValueOf04
 * The benchmark was taken from the repo: 24 January 2018
 */
import org.sosy_lab.sv_benchmarks.Verifier;

public class StringValueOf04 {
  public static Verifier verifier = new Verifier();

  public static void main(String[] args) {
    boolean booleanValue = verifier.nondetBoolean();
    String tmp = String.valueOf(booleanValue);
    assert tmp.equals("true");
  }
}
