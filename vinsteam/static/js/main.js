document.addEventListener("DOMContentLoaded", () => {
  const form = document.getElementById("product-form");

  form.addEventListener("submit", async (event) => {
    event.preventDefault();

    const formData = new FormData(form);
    const csrfToken = formData.get("csrfmiddlewaretoken");

    try {
      const response = await fetch("/api/products/create/", {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
          "X-CSRFToken": csrfToken,
        },
        body: JSON.stringify({
          name: formData.get("name"),
          description: formData.get("description"),
          price: parseFloat(formData.get("price")),
        }),
      });

      if (response.ok) {
        alert("Продукт успешно создан!");
        location.reload();
      } else {
        const result = await response.json();
        let errorMsg = "Ошибка создания продукта:\n";
        if (result.name) {
          errorMsg += `Название: ${result.name[0]}\n`;
        }
        if (result.price) {
          errorMsg += `Цена: ${result.price[0]}\n`;
        }
        alert(errorMsg);
      }
    } catch (error) {
      console.error("Ошибка при создании продукта:", error);
      alert("Произошла ошибка при создании продукта. Пожалуйста, попробуйте снова.");
    }
  });
});
