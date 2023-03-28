PyTestdeki decoratorler;

PyTest Python dilinde yazılmış bir test çerçevesidir. Decoratorlar ise PyTestte test fonksiyonlarını belirlemek ve test davranışını değiştirmek için kullanılır.

PyTestte kullanılan decoratorlar aşağıda yer almaktadır;

* '@pytest.fixture'  ; bu decorator, test fonksiyonları tarafından kullanılabilen bir fixture'ı tanımlamak için kullanılır. Fixture'lar testleri düzenlemek ve tekrar kullanılabilirliği arttırmak için kullanılır.

* '@pytest.mark.parametrize'  ; Bu decorator test fonksiyonunu değişken parametrelerle tekrar kullanmak için kullanılır. Bu decorator kullanılarak, test fonksiyonunu belirli bir parametre kümsei için tekrar çalıştırabiliriz.

* '@pytest.mark.skip'  ; Bu decorator, belirli bir testin atlanması gerektiğinde kullanılır. Bu, testin geçici olarak devre dışı bırakılması veya belirli bir koşul karşılanmadığında testin çalıştırılmaması gerektiği durumlarda kullanılabilir

* @pytest.mark.xfail: Bu decorator, bir testin başarısız olması gerektiğinde kullanılır. Bu, bir hata oluştuğunda veya bir koşulun karşılanmadığında testin beklenen şekilde başarısız olmasını sağlamak için kullanılabilir.

* @pytest.mark.timeout: Bu decorator, bir testin belirli bir sürede tamamlanması gerektiğini belirtmek için kullanılır. Bu, uzun çalışan testlerin tespit edilmesine yardımcı olur ve testlerin zamanında tamamlanmasını sağlar.

* @pytest.mark.filterwarnings: Bu decorator, bir testin belirli bir uyarı mesajını içermesi durumunda testin başarısız olması gerektiğini belirtmek için kullanılır.

* @pytest.mark.usefixtures: Bu decorator, belirli bir fixture'ı test fonksiyonunda kullanmak için kullanılır.

* @pytest.mark.flaky: Bu decorator, belirli bir testin geçici hatalar veya beklenmedik sonuçlar nedeniyle zaman zaman başarısız olabileceğini belirtmek için kullanılır.

* @pytest.mark.run: Bu decorator, belirli bir testin yalnızca belirli koşullar sağlandığında veya belirli bir test grubunda çalıştırılması gerektiğini belirtmek için kullanılır.

* @pytest.mark.dependency: Bu decorator, testler arasındaki bağımlılıkları belirlemek için kullanılır. Bu, bir testin başarılı olması için önceden belirli bir başka testin başarılı * olması gerektiği durumlarda kullanılabilir.

* @pytest.mark.parametrize: Bu decorator, belirli bir parametre kümesi için test fonksiyonunun tekrarlanmasını sağlar.

* @pytest.mark.freeze_time: Bu decorator, belirli bir testin sürekli olarak aynı zamanda çalıştırılmasını sağlamak için kullanılır. Bu, belirli bir testin zamanla değişebileceği durumlarda kullanılabilir.

Bu decorator'lar, pytest'te test sürecini yönetmek ve test davranışını değiştirmek için kullanılabilir.