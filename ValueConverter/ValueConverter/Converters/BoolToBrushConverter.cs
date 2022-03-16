using System;
using System.Collections.Generic;
using System.Globalization;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Data;
using System.Windows.Media;

namespace ValueConverter.Converters
{
    public class BoolToBrushConverter : IValueConverter //CTRL PERIOD WILL USE WHATEVER THING NEEDED
    {
        public object Convert(object value, Type targetType, object parameter, CultureInfo culture)
        {
            var isOnline = (bool)value;
            if (isOnline)
                return Brushes.Green;
            else
                return Brushes.Red;
        }

        public object ConvertBack(object value, Type targetType, object parameter, CultureInfo culture)
        {
            throw new NotImplementedException();
        }
    }
}
