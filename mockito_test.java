import static org.mockito.Mockito.*;
//import org.mockito.ArgumentCaptor;
import java.io.IOException;

public class mockito_test {
  public static void main(String[] args) {
    IntegerBug bug;
    String[] mockArgs = new String[] {"1000"};
    bug = mock(IntegerBug.class);
    doThrow(new IOException()).when(bug).main(mockArgs);
    bug.main(mockArgs);

    //ArgumentCaptor<IntegerBug> argument = ArgumentCaptor.forClass(IntegerBug.class);
    //verify(bug).main(argument.capture());
    //assertEquals(*expected value here*, argument.getValue());
  }
}
