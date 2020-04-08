import React from 'react';

interface DemoData {
  id: number;
  name: string;
}

interface State {
  data: DemoData[];
  loaded: boolean;
  placeholder: string
}

export default class App extends React.Component<{}, State> {
  state: State = {
    data: [],
    loaded: false,
    placeholder: "Loading"
  };

  public componentDidMount(): void {
    fetch("api/demo")
      .then(response => {
        if (response.status > 400) {
          return this.setState(() => {
            return { placeholder: "Something went wrong!" };
          });
        }
        return response.json();
      })
      .then(data => {
        this.setState(() => {
          return {
            data,
            loaded: true
          };
        });
      });
  }

  public render(): JSX.Element {
    return (
      <ul>
        {this.state.data.map(contact => {
          return (
            <li key={contact.id}>
              {contact.name}
            </li>
          );
        })}
      </ul>
    );
  }
}
