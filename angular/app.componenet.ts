import { Component } from '@angular/core';

@Component({
  selector: 'app-root',
  template: `<app-dynamic-form [formConfig]="formFields"></app-dynamic-form>`
})
export class AppComponent {
  formFields = [
    {
      type: "input",
      label: "Product Name",
      placeholder: "Enter product name",
      inputType: "text",
      key: "productName",
      width: "50%"
    },
    {
      type: "input",
      label: "Price",
      placeholder: "Enter price",
      inputType: "number",
      key: "price",
      width: "30%"
    },
    {
      type: "dropdown",
      label: "Category",
      key: "category",
      options: ["Electronics", "Apparel", "Home"],
      width: "50%"
    },
    {
      type: "button",
      label: "Submit",
      action: "submit"
    }
  ];
}
